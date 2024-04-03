import logging
import os
import las
import requests
import json


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


def post_feedback_v2(las_client: las.Client, document_id: str, dataset_id: str, feedback: dict):
    def should_post_feedback(item, label):
        return not item[label].get('automated') or item[label].get('isEdited')

    ground_truth = []

    for label in feedback:
        is_line_item = isinstance(feedback[label], list)
        if is_line_item:
            if not feedback[label]:
                # Ignore blank lines
                continue
            
            lines = []
            for line in feedback[label]:
                line_gt = []
                for line_label in line:
                    if should_post_feedback(line, line_label):
                        line_gt += [{
                            'label': line_label,
                            'value': line[line_label]['value'],
                            'pages': line[line_label]['pages']
                        }]

                lines += [line_gt]

            ground_truth += [{
                'label': label,
                'value': lines,
            }]
        else:
            # This is a non-line item field
            if should_post_feedback(feedback, label):
                ground_truth += [{
                    'label': label,
                    'value': feedback[label]['value'],
                    'pages': feedback[label]['pages']
                }]

    las_client.update_document(
        document_id=document_id,
        ground_truth=ground_truth,
        dataset_id=dataset_id
    )
    

def parse_webhook_endpoints(s):
    if not s: return []

    try:
        webhook_endpoints = json.loads(s)
        if isinstance(webhook_endpoints, list):
            return webhook_endpoints
    except RuntimeError:
        logging.error('Unable to JSON decode webhook endpoints')
    
    return []


@las.transition_handler
def feedback_and_export(las_client, event):
    document_id = event['documentId']
    dataset_id = os.environ.get('DATASET_ID')
    validated = event.get('needsValidation') is True
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
    }

    webhook_endpoints = []
    if webhooks := os.environ.get('WEBHOOK_ENDPOINTS'):
        webhook_endpoints = parse_webhook_endpoints(webhooks)
    elif uri := os.environ.get('WEBHOOK_URI'):
        webhook_endpoints = [{'uri': uri}]

    for endpoint in webhook_endpoints:
        logging.info(f'Posting result to {endpoint}...')
        requests.post(endpoint['uri'], json=response)

    return response
