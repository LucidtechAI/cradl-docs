def required_labels(field_config):
    return {label for label in field_config if field_config[label].get('required', True)}


def is_line(field_config, p):
    return field_config.get(p['label'], {}).get('type') == 'lines'


def is_enum(field_config, p):
    return field_config.get(p['label'], {}).get('type') == 'enum'


# def get_labels(predictions):
#     return set([p['label'] for p in predictions])

def get_labels(form_config):
    return {label for label in form_config.keys()}


def get_line_labels(form_config):
    return {line_label for label, config in form_config.items() if config.get('type') == 'lines' for line_label in config['fields']}


def filter_optional_fields(predictions, field_config):
    def predicate(p):
        if is_line(field_config, p):
            return True
        conf_threshold = field_config.get(p['label'], {}).get('confidenceLevels', {}).get('low', 0.3)
        return p['label'] in required_labels(field_config) or conf_threshold < p['confidence']
    
    return list(filter(predicate, predictions))


def filter_by_top1(predictions, labels, line_labels=None):
    labels = set([p['label'] for p in predictions])
    def top1(predictions, label):
        field_preds = [p for p in predictions if p['label'] == label]
        return max(field_preds, key=lambda p: p.get('confidence', 1.0)) if field_preds else None

    result = []
    for label in labels:
        top_preds = top1(predictions, label)
        if isinstance(top_preds['value'], list):
            lines = []
            for line in top_preds['value']:
                lines += [filter_by_top1(line, line_labels)]
            
            top_preds['value'] = lines

        if top_preds:
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
            value = old_ground_truth.pop(label, prediction['value'])
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


def overlap(last_lines, first_lines):
    for first_line in first_lines:
        for last_line in last_lines:
            if first_line['label'] == last_line['label'] and first_line['value'] != last_line['value']:
                return False
    return True


def merge_lines(last_line, first_line):
    return last_line + first_line


def merge_lines_from_different_pages(predictions, field_config):
    line_labels = [field for field, config in field_config.items() if config['type'] == 'lines']

    if not line_labels:
        return predictions

    line_predictions = {line_field: [] for line_field in line_labels}

    merged_predictions = []
    for prediction in predictions:
        label = prediction['label']
        if label in line_labels:
            line_values = prediction['value']

            # Check lines within the prediction (can have up to 3 pages within a prediction)
            previous_line = line_values[0]
            previous_page = previous_line[0]['page']  # assume all fields in the line is from the same page

            for index, line in enumerate(line_values[1:], start=1):
                current_page = line[0]['page']
                if previous_page != current_page:
                    if overlap(previous_line, line):
                        line = merge_lines(previous_line, line)
                        line_values[index] = line
                        line_values[index - 1] = []
                previous_page = current_page
                previous_line = line
            line_values = [line for line in line_values if line]

            # Check lines from last page in previous predicted pages
            previously_predicted_line = line_predictions[label][-1] if line_predictions[label] else []
            first_line = line_values[0]
            if overlap(previously_predicted_line, first_line):
                line_values[0] = merge_lines(previously_predicted_line, first_line)
                if line_predictions[label]:  # Need to check if any lines have been processed
                    line_predictions[label].pop()

            line_predictions[label].extend(line_values)
        else:
            merged_predictions.append(prediction)

    merged_predictions += [{'label': k, 'value': v} for k, v in line_predictions.items()]

    return merged_predictions


def patch_empty_predictions(predictions, labels, no_empty_prediction_fields):
    empty_predictions = {label: [] for label in labels if label not in no_empty_prediction_fields}
    patched_predictions = []
    for prediction in predictions:
        if prediction['value'] is not None:
            patched_predictions.append(prediction)
        elif prediction['label'] not in no_empty_prediction_fields:
            empty_predictions[prediction['label']].append(prediction)

    min_empty_predictions = [min(v, key=lambda p: p.get('confidence', 0.0)) for v in empty_predictions.values() if v]
    patched_predictions += min_empty_predictions

    return patched_predictions


