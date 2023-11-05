import logging
import os
import las
import json
import base64

from .utils import *


logging.getLogger().setLevel(logging.INFO)


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


@las.transition_handler
def make_predictions(las_client, event):
    document_id = event['documentId']
    model_id = os.environ['MODEL_ID']
    form_config_id = os.environ['FORM_CONFIG_ASSET_ID']
    
    logging.info(f'Processing event:')
    logging.info(json.dumps(event, indent=2))

    form_config_asset = las_client.get_asset(form_config_id)
    form_config = json.loads(base64.b64decode(form_config_asset['content']))
    
    output = {}
    needs_validation = True

    try:
        predictions = las_client.create_prediction(document_id, model_id).get('predictions')
        logging.info(f'Created predicitons {predictions}')

        old_ground_truth = las_client.get_document(document_id=document_id).get('groundTruth')

        if predictions:
            field_config = form_config['config']['fields']
            top1_preds = filter_by_top1(predictions)

            all_above_threshold_or_optional = True
            for prediction in top1_preds:
                if is_line(field_config, prediction):
                    label = prediction['label']
                    line_field_config = field_config[label]['fields']

                    for line in prediction['value']:
                        # Check that each prediction on each line is above threshold or optional
                        for line_pred in line:
                            if not above_threshold_or_optional(line_pred, line_field_config):
                                all_above_threshold_or_optional = False

                elif not above_threshold_or_optional(prediction, field_config):
                    all_above_threshold_or_optional = False

            has_all_required_labels = required_labels(field_config) <= set(map(lambda p: p['label'], predictions))
            needs_validation = not has_all_required_labels or not all_above_threshold_or_optional

            logging.info(f'All predictions above threshold (or optional): {all_above_threshold_or_optional}')
            logging.info(f'All required labels exist: {has_all_required_labels}')
            
            # Filter out optional fields where confidence < low
            predictions = filter_optional_fields(predictions, field_config)

            if old_ground_truth:
                predictions = merge_predictions_and_gt(predictions, old_ground_truth, field_config)
                logging.info(f'updated predictions: {predictions}')

            output = {'predictions': predictions}
            if not needs_validation:
                output['verified'] = format_verified_output(filter_optional_fields(top1_preds, field_config))

        elif old_ground_truth:
            old_ground_truth = {gt['label']: gt['value'] for gt in old_ground_truth}
            output = {'predictions': add_confidence_to_ground_truth(old_ground_truth)}

    except las.client.BadRequest as e:
        logging.exception(e)
    
    return {
        'documentId': document_id,
        'needsValidation': needs_validation,
        **output
    }
