import logging
import os
import las
import requests

from .utils import parse_webhook_endpoints, convert_predictions_to_v2, to_validated_format


logging.getLogger().setLevel(logging.INFO)


def post_feedback_v1(las_client: las.Client, document_id: str, dataset_id: str, verified: dict):
    document = las_client.get_document(document_id=document_id)
    old_ground_truth = {g['label']: g['value'] for g in document.get('groundTruth', [])}

    new_ground_truth = {**old_ground_truth, **verified}

    ground_truth = []
    for label, value in new_ground_truth.items():
        if isinstance(value, list):
            if not value:
                continue  # Do not write completely empty lines to GT
            if not isinstance(value[0], list):
                value = [[{'label': k, 'value': v} for k, v in line_pred.items()] for line_pred in value]
        ground_truth.append({
            'label': label,
            'value': value,
        })

    las_client.update_document(
        document_id=document_id,
        ground_truth=ground_truth,
        dataset_id=dataset_id
    )


def _create_gt_dict(label, gt_info):
    gt_dict = {
        'label': label,
        'value': gt_info.get('rawValue', gt_info.get('value')),
        'pages': gt_info.get('pages') or []
    }

    if 'confidence' in gt_info:
        gt_dict['confidence'] = 1.0 if gt_info.get('isEdited', False) else gt_info['confidence']
    return gt_dict


def post_feedback_v2(las_client: las.Client, document_id: str, dataset_id: str, feedback: dict, field_config: dict):
    document = las_client.get_document(document_id=document_id)
    old_ground_truth = {g['label']: {**g, 'isOldGt': True} for g in document.get('groundTruth', [])}
    ground_truth = []

    for label, value in {**old_ground_truth, **feedback}.items():
        config = field_config.get(label)
        if not config:
            logging.info(f'Could not find entry for label {label} in fieldConfig, skipping...')
            continue

        if config['type'] == 'lines':
            if not value:
                continue  # Ignore blank lines

            lines = []
            for line in value:
                line_gt = []
                for line_label, line_values in line.items():
                    line_config = config.get('fields', {}).get(line_label, {})
                    if line_config.get('isMultivalue', False):
                        for line_value in line_values:
                            line_gt.append(_create_gt_dict(line_label, line_value))
                    else:
                        line_gt.append(_create_gt_dict(line_label, line_values))
                lines.append(line_gt)

            ground_truth.append({'label': label, 'value': lines})
        else:
            if config.get('isMultivalue', False):
                for v in value:
                    ground_truth.append(_create_gt_dict(label, v))
            else:
                ground_truth.append(_create_gt_dict(label, value))

    las_client.update_document(
        document_id=document_id,
        ground_truth=ground_truth,
        dataset_id=dataset_id
    )


@las.transition_handler
def feedback_and_export(las_client, event):
    document_id = event['documentId']
    dataset_id = os.environ.get('DATASET_ID')
    model_id = os.environ.get('MODEL_ID')
    validated = event.get('needsValidation', True)
    feedback_v1 = event.get('verified')
    feedback_v2 = event.get('validatedPredictions')

    model = las_client.get_model(model_id)
    predictions = convert_predictions_to_v2(event.get('predictions'), model['fieldConfig'])

    try:
        logging.info(f'Posting feedback to document {document_id} of dataset {dataset_id} ...')

        if feedback_v2:
            post_feedback_v2(
                las_client=las_client,
                document_id=document_id,
                dataset_id=dataset_id,
                feedback=feedback_v2 if validated else {},
                field_config=model['fieldConfig'],
            )
        elif feedback_v1:
            post_feedback_v1(las_client, document_id, dataset_id, feedback_v1 if validated else {})
    except Exception as e:
        logging.exception(e)

    response = {
        'documentId': document_id,
        'values': feedback_v1,
        'validatedPredictions': feedback_v2 if feedback_v2 else to_validated_format(predictions, model['fieldConfig']),
        'predictions': predictions
    }

    if metadata := event.get('metadata'):
        response['metadata'] = metadata

    if dataset_id:
        response['datasetId'] = dataset_id

    webhook_endpoints = []
    if webhooks := os.environ.get('WEBHOOK_ENDPOINTS'):
        webhook_endpoints = parse_webhook_endpoints(webhooks)
    elif uri := os.environ.get('WEBHOOK_URI'):  # For backwards compatibility
        webhook_endpoints = [{'uri': uri}]

    request_exception = None
    for endpoint in webhook_endpoints:
        logging.info(f'Posting result to {endpoint}...')
        try:
            res = requests.post(endpoint['uri'], json=response, headers=endpoint.get('headers'))
        except (requests.exceptions.RequestException, KeyError) as re:
            logging.exception(re)
            request_exception = re
            continue

        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as re:
            logging.exception(re)
            request_exception = re
            logging.error(res.content)

    if request_exception:
        raise request_exception

    return response
