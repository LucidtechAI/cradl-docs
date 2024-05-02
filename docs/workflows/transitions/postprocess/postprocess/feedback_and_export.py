import logging
import os
import las
import requests

from .utils import parse_webhook_endpoints, convert_predictions_to_v2


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
        'value': gt_info.get('rawValue', gt_info['value']),
        'pages': gt_info.get('pages')
    }

    if 'confidence' in gt_info:
        gt_dict['confidence'] = 1.0 if gt_info.get('isEdited', False) else gt_info['confidence']
    return gt_dict


def post_feedback_v2(las_client: las.Client, document_id: str, dataset_id: str, feedback: dict):
    document = las_client.get_document(document_id=document_id)
    old_ground_truth = {g['label']: {**g, 'isOldGt': True} for g in document.get('groundTruth', [])}

    def should_post_feedback(v):
        return True

    ground_truth = []

    for label, value in {**old_ground_truth, **feedback}.items():
        is_line_item = isinstance(value, list)
        if is_line_item:
            if not value:
                # Ignore blank lines
                continue

            lines = []
            for line in value:
                line_gt = [_create_gt_dict(_l, _v) for _l, _v in line.items() if should_post_feedback(_v)]
                lines.append(line_gt)

            ground_truth.append({'label': label, 'value': lines})
        elif should_post_feedback(value):
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
    validated = event.get('needsValidation', True) is True
    feedback_v1 = event.get('verified')
    feedback_v2 = event.get('validatedPredictions')

    try:
        logging.info(f'Posting feedback to dataset {dataset_id} ...')

        if feedback_v2:
            post_feedback_v2(las_client, document_id, dataset_id, feedback_v2 if validated else {})
        elif feedback_v1:
            post_feedback_v1(las_client, document_id, dataset_id, feedback_v1 if validated else {})
    except Exception as e:
        logging.exception(e)

    response = {
        'documentId': document_id,
        'datasetId': dataset_id,
        'values': feedback_v1,
        'validatedPredictions': feedback_v2,
        'predictions': convert_predictions_to_v2(event.get('predictions'))
    }

    webhook_endpoints = []
    if webhooks := os.environ.get('WEBHOOK_ENDPOINTS'):
        webhook_endpoints = parse_webhook_endpoints(webhooks)
    elif uri := os.environ.get('WEBHOOK_URI'):
        webhook_endpoints = [{'uri': uri}]

    request_exception = None
    for endpoint in webhook_endpoints:
        logging.info(f'Posting result to {endpoint}...')
        try:
            requests.post(endpoint['uri'], json=response)
        except (requests.exceptions.RequestException, KeyError) as re:
            request_exception = re

    if request_exception:
        raise request_exception

    return response
