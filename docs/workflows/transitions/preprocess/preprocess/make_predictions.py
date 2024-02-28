import logging
import os
import las
import json
import base64

from .utils import *


logging.getLogger().setLevel(logging.INFO)


@las.transition_handler
def make_predictions(las_client, event):
    document_id = event['documentId']
    model_id = os.environ['MODEL_ID']
    form_config_id = os.environ['FORM_CONFIG_ASSET_ID']

    logging.info('Processing event:')
    logging.info(json.dumps(event, indent=2))

    form_config_asset = las_client.get_asset(form_config_id)
    form_config = json.loads(base64.b64decode(form_config_asset['content']))

    model = las_client.get_model(model_id)
    model_metadata = model.get('metadata', {})
    preprocess_config = model.get('preprocessConfig', {})
    logging.info(f'model metadata: {model_metadata}')

    output = {}
    needs_validation = True

    labels = get_labels(form_config['config']['fields'])
    no_empty_prediction_fields = set()

    if not (predictions := event.get('predictions')):
        start_page = 0
        predictions = []
        while start_page is not None and start_page < model_metadata.get('maxPredictionPages', 100):
            try:
                preprocess_config['startPage'] = start_page
                current_prediction = las_client.create_prediction(
                    document_id=document_id,
                    model_id=model_id,
                    preprocess_config=preprocess_config,
                )
                start_page = current_prediction.get('nextPage')
                current_prediction = current_prediction['predictions']

                fields_with_empty_prediction = set(
                    prediction['label'] for prediction in current_prediction if prediction['value'] is None
                )
                no_empty_prediction_fields = no_empty_prediction_fields.union(labels - fields_with_empty_prediction)

                predictions.extend(current_prediction)
                logging.info(f'new start_page {start_page}')
            except Exception as e:
                logging.exception(e)
                break

    logging.info(f'Created predictions {predictions}')

    try:
        old_ground_truth = las_client.get_document(document_id=document_id).get('groundTruth')

        if predictions:
            field_config = form_config['config']['fields']
            column_names = get_column_names(field_config)
            labels = labels.union(column_names)
            top1_preds = filter_by_top1(predictions, labels)

            if model_metadata.get('mergeContinuedLines'):
                predictions = merge_lines_from_different_pages(predictions, field_config)

            predictions = patch_empty_predictions(predictions, labels, no_empty_prediction_fields)
            predictions = filter_away_low_confidence_lines(predictions, field_config)

            logging.info(f'patched and filtered predictions {predictions}')

            all_above_threshold_or_optional = True
            if threshold_is_zero_for_all(field_config):
                needs_validation = False
                has_all_required_labels = True
            else:
                for prediction in top1_preds:
                    if is_line(field_config, prediction):
                        label = prediction['label']
                        line_field_config = field_config[label]['fields']

                        for line in prediction['value']:
                            # Check that each prediction on each line is above threshold or optional
                            if not line and field_config[label].get('required', True):
                                all_above_threshold_or_optional = False
                            for line_pred in line:
                                if not above_threshold_or_optional(line_pred, line_field_config):
                                    all_above_threshold_or_optional = False
                        continue
                    if is_enum(field_config, prediction) and prediction['value'] is None:
                        # Need to validate correct enum value, unless automation level is zero.
                        prediction['confidence'] = 0.0
                    if not above_threshold_or_optional(prediction, field_config):
                        all_above_threshold_or_optional = False

                has_all_required_labels = required_labels(field_config) <= set(map(lambda p: p['label'], predictions))
                needs_validation = not has_all_required_labels or not all_above_threshold_or_optional

            logging.info(f'All predictions above threshold (or optional): {all_above_threshold_or_optional}')
            logging.info(f'All required labels exist: {has_all_required_labels}')

            # Filter out optional fields where confidence < low
            predictions = filter_optional_fields(predictions, field_config)

            if old_ground_truth:
                predictions = merge_predictions_and_gt(predictions, old_ground_truth, field_config)
                logging.info(f'Updated predictions: {predictions}')

            output = {'predictions': predictions}
            if not needs_validation:
                output['verified'] = format_verified_output(filter_optional_fields(top1_preds, field_config))

        elif old_ground_truth:
            old_ground_truth = {gt['label']: gt['value'] for gt in old_ground_truth}
            output = {'predictions': add_confidence_to_ground_truth(old_ground_truth)}
        else:
            output = {'predictions': predictions}

    except las.client.BadRequest as e:
        logging.exception(e)

    if email_context := event.get('email'):
        subject = email_context.get('subject') or ''
        origin = email_context.get('origin') or ''
        header = f'{subject} (From: {origin})'
        output.update({
            'leadingTextHeader': {'value': header},
            'leadingText': {'value': email_context.get('body') or ''},
        })

    logging.info(f'output: {output}')

    return {
        'documentId': document_id,
        'needsValidation': needs_validation,
        **output
    }
