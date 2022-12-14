import logging
import os
import las
import json
import base64


def required_labels(field_config):
    return set([label for label in field_config if field_config[label].get('required', True)])


@las.transition_handler
def make_predictions(las_client, event):
    document_id = event['documentId']
    model_id = os.environ['MODEL_ID']
    field_config_id = os.environ['FIELD_CONFIG_ASSET_ID']
    
    logging.info(f'Processing event:')
    logging.info(json.dumps(event, indent=2))

    field_config_asset = las_client.get_asset(field_config_id)
    field_config = json.loads(base64.b64decode(field_config_asset['content']))
    
    output = {}
    skip_validation = False

    try:
        predictions = las_client.create_prediction(document_id, model_id).get('predictions')
        logging.info(f'Created predicitons {predictions}')

        if predictions:
            def above_threshold_or_optional(prediction):
                label, confidence = prediction['label'], prediction['confidence']
                threshold = field_config[label]['confidenceLevels']
                is_optional = not field_config[label].get('required', True)

                return (threshold['automated'] <= confidence) or (is_optional and confidence < threshold['low'])
            
            all_above_or_optional = all(map(above_threshold_or_optional, predictions))
            has_all_required_labels = required_labels(field_config) <= set(map(lambda p: p['label'], predictions))
            skip_validation = has_all_required_labels and all_above_or_optional
            
            logging.info(f'All predictions above threshold (or optional): {all_above_or_optional}')
            logging.info(f'All required labels exist: {has_all_required_labels}')

            output = {'predictions': predictions}
    except las.client.BadRequest as e:
        logging.exception(e)
    
    if skip_validation:
        output['verified'] = {p['label']: p['value'] for p in predictions} 
        output['validationSkipped'] = True

    return {
        'documentId': document_id,
        'needsValidation': not skip_validation,
        **output
    }