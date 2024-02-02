import numpy as np


MINIMUM_AVERAGE_LINE_CONFIDENCE = 0.3


def required_labels(field_config):
    return {label for label in field_config if field_config[label].get('required', True)}


def is_line(field_config, p):
    return field_config.get(p['label'], {}).get('type') == 'lines'


def is_enum(field_config, p):
    return field_config.get(p['label'], {}).get('type') == 'enum'


def get_labels(form_config):
    return {label for label in form_config.keys()}


def get_column_names(form_config):
    return {
        column for label, config in form_config.items() if config.get('type') == 'lines' for column in config['fields']
    }


def filter_optional_fields(predictions, field_config):
    def predicate(p):
        if is_line(field_config, p):
            return True
        conf_threshold = field_config.get(p['label'], {}).get('confidenceLevels', {}).get('low', 0.3)
        return p['label'] in required_labels(field_config) or conf_threshold < p['confidence']
    
    return list(filter(predicate, predictions))


def filter_by_top1(predictions, labels):
    def top1(predictions, label):
        field_preds = [p for p in predictions if p['label'] == label]
        return max(field_preds, key=lambda p: p.get('confidence', 1.0)) if field_preds else None

    result = []
    for label in labels:
        top_preds = top1(predictions, label)
        if top_preds:
            if isinstance(top_preds['value'], list):
                top_preds['value'] = [filter_by_top1(line, labels) for line in top_preds['value']]

            result += [top_preds]

    return result
    

def above_threshold_or_optional(prediction, field_config):
    label, confidence = prediction['label'], prediction.get('confidence')
    if label not in field_config:
        return False

    threshold = field_config[label]['confidenceLevels']
    is_optional = not field_config[label].get('required', True)

    return (threshold['automated'] <= confidence) or (is_optional and confidence < threshold['low'])


def format_verified_output(top1_preds):
    result = {}
    for pred in top1_preds:
        if isinstance(pred['value'], list):
            fmt_lines = []
            for line in pred['value']:
                fmt_lines += [{p['label']: p['value'] for p in line}]

            result[pred['label']] = fmt_lines
        else:
            result[pred['label']] = pred['value']

    return result


def add_confidence_to_ground_truth(ground_truth):
    updated_ground_truth = []
    for key, value in ground_truth.items():
        gt = {'label': key, 'value': value}
        if isinstance(value, list):
            for line in gt['value']:
                for line_pred in line:
                    line_pred['confidence'] = 1.0
        else:
            gt['confidence'] = 1.0
        updated_ground_truth.append(gt)

    return updated_ground_truth


def merge_predictions_and_gt(predictions, old_ground_truth, field_config):
    old_ground_truth = {gt['label']: gt['value'] for gt in old_ground_truth}
    updated_predictions = []
    updated_labels = set()

    # override value if label is the same, add if it is not predicted
    for prediction in predictions:
        label = prediction['label']
        if label in updated_labels:
            continue
        if label in old_ground_truth:
            updated_labels.add(label)
            value = old_ground_truth.pop(label)
            confidence = None
            if is_line(field_config, prediction):
                for line in value:
                    for line_pred in line:
                        line_pred['confidence'] = 1.0
            else:
                confidence = 1.0
        else:
            value = prediction['value']
            confidence = prediction['confidence'] if not is_line(field_config, prediction) else None
        updated_prediction = {
            'label': label,
            'value': value,
        }
        if confidence:
            updated_prediction['confidence'] = confidence
        updated_predictions.append(updated_prediction)

    updated_predictions += add_confidence_to_ground_truth(old_ground_truth)

    return updated_predictions


def overlap(line_1, line_2, column_names):
    """
    Checks for overlapping lines.
    The two lines are overlapping if the missing fields from line_1 is present in line_2 and visa versa, or, if
    the value of the line field is the same for both lines for the same field (this includes empty values for both
    lines).
    """
    line_1 = filter_by_top1(line_1, column_names)
    line_2 = filter_by_top1(line_2, column_names)
    for p in line_1:
        for q in line_2:
            if p['label'] == q['label'] and p['value'] != q['value']:
                return False
    return True


def _merge_lines(line_1, line_2):
    # line_1 and line_2 can have overlapping values. We keep all values, and the one with the highest confidence is
    # used later on.
    return line_1 + line_2


def merge_lines_from_different_pages(predictions, field_config):
    line_labels = [field for field, config in field_config.items() if config['type'] == 'lines']

    if not line_labels:
        return predictions

    # Each p in prediction can have lines from up to 3 pages. We first add all lines from all pages in one large list.
    # We then iterate this list, and check if the lines across different pages can be merged.
    line_predictions = {line_label: [] for line_label in line_labels}
    for p in predictions:
        if p['label'] in line_labels:
            line_predictions[p['label']].extend(p['value'])

    column_names = get_column_names(field_config)

    for line_label, line_values in line_predictions.items():
        if not line_values or not line_values[0]:
            continue

        previous_line = line_values[0]
        previous_page = previous_line[0]['page']  # assume all fields in the line is from the same page

        for index, line in enumerate(line_values[1:], start=1):
            current_page = line[0]['page']
            if previous_page != current_page and overlap(previous_line, line, column_names):
                line = _merge_lines(previous_line, line)
                line_values[index] = line
                line_values[index - 1] = None
            previous_page = current_page
            previous_line = line
        line_predictions[line_label] = [line for line in line_values if line]

    merged_predictions = [p for p in predictions if p['label'] not in line_labels]
    merged_predictions += [{'label': k, 'value': v} for k, v in line_predictions.items()]

    return merged_predictions


def patch_empty_predictions(predictions, labels, no_empty_prediction_fields):
    """
    If we have a document with more than 3 pages, we can have that we get no empty prediction for a field for the
    first 3 pages, but for the next pages we can have empty predictions. This can for instance be the case
    if supplier_name is written on page 0 (we will then not get any empty predictions for page 0 - 2), but
    there are no supplier_name written on the other pages (so we will get an empty prediction for page 2 >). In this
    case, we want to filter out all empty predictions. We will then add the field to no_empty_prediction_fields
    and only return non-empty predictions.

    In other cases, we want to use the empty prediction value with the minimum confidence value, so that we do
    not overwrite other predictions.
    TODO: Is this still the case with the new fix in las-workspace?
    """
    empty_predictions = {label: [] for label in labels if label not in no_empty_prediction_fields}
    patched_predictions = []
    for prediction in predictions:
        if prediction['value'] is not None:
            patched_predictions.append(prediction)
        elif prediction['label'] not in no_empty_prediction_fields:
            empty_predictions[prediction['label']].append(prediction)

    min_empty_predictions = [min(v, key=lambda p: p['confidence']) for v in empty_predictions.values() if v]
    patched_predictions += min_empty_predictions

    return patched_predictions


def filter_away_low_confidence_lines(predictions, field_config):
    column_names = {
        label: {column_name for column_name in config['fields']}
        for label, config in field_config.items() if config.get('type') == 'lines'
    }

    for prediction in predictions:
        label = prediction['label']
        if field_config.get(label, {}).get('type') == 'lines':
            line_predictions = []
            for line in prediction['value']:
                top_1_prediction = filter_by_top1(line, column_names[label])

                # column names that are not present in the line counts as 0% confidence
                line_columns_present = {p['label'] for p in top_1_prediction}
                top_1_prediction += [{'confidence': 0.0} for _ in column_names[label] - line_columns_present]
                average_confidence = np.mean([line_dict['confidence'] for line_dict in top_1_prediction])
                if average_confidence >= MINIMUM_AVERAGE_LINE_CONFIDENCE:
                    line_predictions.append(line)
            line_predictions = line_predictions or [[]]  # still need one empty list if all lines are removed
            prediction['value'] = line_predictions

    return predictions
