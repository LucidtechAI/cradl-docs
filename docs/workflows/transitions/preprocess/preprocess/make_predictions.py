import logging
import os
import las
import json
import base64


logging.getLogger().setLevel(logging.INFO)


def required_labels(field_config):
    return set([label for label in field_config if field_config[label].get('required', True)])


def filter_optional_fields(predictions, field_config):
    def predicate(p):
        conf_threshold = field_config[p['label']]['confidenceLevels']['low']
        return p['label'] in required_labels(field_config) or conf_threshold < p['confidence']
    
    return list(filter(predicate, predictions))


def filter_by_top1(predictions):
    labels = set(map(lambda p: p['label'], predictions))
    
    def top1(label):
        preds = filter(lambda f: f['label'] == label, predictions)
        return max(preds, key=lambda p: p['confidence'])

    return [top1(label) for label in labels]


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
    skip_validation = False

    try:
        predictions = las_client.create_prediction(document_id, model_id).get('predictions')
        logging.info(f'Created predicitons {predictions}')

        if predictions:
            field_config = form_config['config']['fields']

            def above_threshold_or_optional(prediction):
                label, confidence = prediction['label'], prediction['confidence']
                threshold = field_config[label]['confidenceLevels']
                is_optional = not field_config[label].get('required', True)

                return (threshold['automated'] <= confidence) or (is_optional and confidence < threshold['low'])
            
            all_above_or_optional = all(map(above_threshold_or_optional, filter_by_top1(predictions)))
            has_all_required_labels = required_labels(field_config) <= set(map(lambda p: p['label'], predictions))
            skip_validation = has_all_required_labels and all_above_or_optional
            
            logging.info(f'All predictions above threshold (or optional): {all_above_or_optional}')
            logging.info(f'All required labels exist: {has_all_required_labels}')
            
            # Filter out optional fields where confidence < low
            predictions = filter_optional_fields(predictions, field_config)
            output = {'predictions': predictions}
    except las.client.BadRequest as e:
        logging.exception(e)
    
    if skip_validation:
        output['verified'] = {p['label']: p['value'] for p in predictions} 

    return {
        'documentId': document_id,
        'needsValidation': not skip_validation,
        **output
    }