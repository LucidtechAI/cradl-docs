import logging
import os
import las
import json
import base64
import requests


def post_feedback(las_client: las.Client, document_id: str, dataset_id: str, verified: dict):
    logging.info(f'Posting feedback to dataset {dataset_id}: {verified}...')

    try:
        ground_truth = [{'label': k, 'value': v} for k, v in verified.items()]

        response = las_client.update_document(
            document_id=document_id,
            ground_truth=ground_truth,
            dataset_id=dataset_id
        )
    except Exception as e:
        logging.exception(e)
        raise


@las.transition_handler
def feedback_and_export(las_client, event):
    document_id = event['documentId']
    verified = event['verified']
    dataset_id = os.environ.get('DATASET_ID')
    skipped_validation = not event['needsValidation']
    
    post_feedback(las_client, document_id, dataset_id, verified if not skipped_validation else {})

    response = {'documentId': document_id, 'datasetId': dataset_id, 'values': verified}
    
    if webhook_uri := os.environ.get('WEBHOOK_URI'):
        logging.info(f'Posting result to {webhook_uri}...')
        requests.post(webhook_uri, json=response)
    
    return response
