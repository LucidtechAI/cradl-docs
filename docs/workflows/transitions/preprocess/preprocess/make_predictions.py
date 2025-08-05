import base64
import copy
import io
import json
import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial

import las
from backoff import constant, on_exception
from pypdf import PdfReader

from .utils import (
    above_threshold_or_optional,
    add_confidence_to_ground_truth,
    create_form_config_from_model,
    filter_optional_fields,
    format_verified_output,
    get_labels,
    is_enum,
    is_line,
    merge_predictions_and_gt,
    patch_and_filter_predictions,
    required_labels,
    threshold_is_zero_for_all,
)


logging.getLogger().setLevel(logging.INFO)


def _fatal_code(e):
    return 400 <= e.response.status_code < 500


# Using a constant interval of 30 seconds between tries. Jitter needs to be None to make sure the interval is
# constant, if not a random number <= 30 will be used.
@on_exception(constant, las.client.TooManyRequestsException, max_tries=6, interval=30, jitter=None)
@on_exception(constant, las.client.RequestException, max_tries=6, giveup=_fatal_code, interval=30, jitter=None)
def _create_prediction(las_client, document_id, model_id, preprocess_config):
    return las_client.create_prediction(
        document_id=document_id,
        model_id=model_id,
        preprocess_config=preprocess_config,
    )


def get_num_pages(las_client, document_id, max_prediction_pages):
    document = las_client.get_document(document_id)
    pdf = PdfReader(io.BytesIO(base64.b64decode(document['content'])))
    return min(len(pdf.pages), max_prediction_pages)


def add_info_from_field_config(form_config, field_config):
    try:
        for key, value in field_config.items():
            form_config['config']['fields'][key]['required'] = value.get('required', True)
        return form_config
    except Exception as e:
        logging.error(f'Error adding info from field config: {e}')
        return form_config


@las.transition_handler
def make_predictions(las_client, event):
    document_id = event['documentId']
    model_id = os.environ['MODEL_ID']
    form_config_id = os.environ['FORM_CONFIG_ASSET_ID']
    max_workers = int(os.environ.get('MAX_WORKERS', '2'))

    logging.info('Processing event:')
    logging.info(json.dumps(event, indent=2))

    form_config_asset = las_client.get_asset(form_config_id)
    form_config = json.loads(base64.b64decode(form_config_asset['content']))

    model = las_client.get_model(model_id)
    model_metadata = model.get('metadata', {})
    preprocess_config = model.get('preprocessConfig', {})
    preprocess_config['maxPages'] = 1
    model_field_config = model.get('fieldConfig', {})
    max_prediction_pages = model_metadata.get('maxPredictionPages', 100)
    logging.info(f'model metadata: {model_metadata}')

    output = {}
    needs_validation = True

    form_config_labels = get_labels(form_config['config']['fields'])
    labels = get_labels(model_field_config)

    if form_config_labels != labels:
        # model has been updated, but form config has not been updated
        form_config = create_form_config_from_model(model_field_config, form_config)
        logging.info(f'\nlabels in fieldConfig does not match form_config. Updated form_config used is: {form_config}')

    form_config = add_info_from_field_config(form_config, model_field_config)

    no_empty_prediction_fields = set()

    if not (predictions := event.get('predictions')):
        prediction_fn = partial(
            _create_prediction,
            las_client=las_client,
            document_id=document_id,
            model_id=model_id,
        )
        try:
            num_pages = get_num_pages(las_client, document_id, max_prediction_pages)
        except Exception as e:
            logging.exception(e)
            num_pages = None

        if num_pages:
            predictions = []
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {}
                for start_page in range(num_pages):
                    config = copy.deepcopy(preprocess_config)
                    config['startPage'] = start_page
                    futures[executor.submit(prediction_fn, preprocess_config=config)] = start_page
                results = {}
                for future in as_completed(futures):
                    try:
                        current_prediction = future.result()['predictions']
                        start_page = futures[future]
                        logging.info(f'Finished predictions for start_page: {start_page}')
                        fields_with_empty_prediction = set(
                            prediction['label'] for prediction in current_prediction if prediction['value'] is None
                        )
                        no_empty_prediction_fields = no_empty_prediction_fields.union(
                            labels - fields_with_empty_prediction
                        )
                        results[start_page] = current_prediction
                    except Exception as e:
                        logging.exception(e)
                for i, prediction in sorted(results.items()):
                    logging.info(f'Extending predictions list with predictions from page {i}')
                    predictions.extend(prediction)

        else:
            start_page = 0
            predictions = []
            while start_page is not None and start_page < max_prediction_pages:
                try:
                    preprocess_config['startPage'] = start_page
                    current_prediction = prediction_fn(preprocess_config=preprocess_config)
                    start_page = current_prediction.get('nextPage')
                    current_prediction = current_prediction['predictions']

                    fields_with_empty_prediction = set(
                        prediction['label'] for prediction in current_prediction if prediction['value'] is None
                    )
                    no_empty_prediction_fields = no_empty_prediction_fields.union(
                        labels - fields_with_empty_prediction
                    )

                    predictions.extend(current_prediction)
                    logging.info(f'new start_page {start_page}')
                except Exception as e:
                    logging.exception(e)
                    break

    logging.info(f'Created predictions {predictions}')

    try:
        old_ground_truth = las_client.get_document(document_id=document_id).get('groundTruth')
    except Exception as e:
        logging.exception(e)
        old_ground_truth = None

    try:
        if predictions:
            field_config = form_config['config']['fields']
            predictions, top1_preds = patch_and_filter_predictions(
                predictions=predictions,
                field_config=field_config,
                labels=labels,
                merge_continued_lines=model_metadata.get('mergeContinuedLines'),
                no_empty_prediction_fields=no_empty_prediction_fields,
            )
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
                _required_labels = required_labels(field_config)
                _top_1_labels = set(map(lambda p: p['label'], top1_preds))
                has_all_required_labels = _required_labels <= _top_1_labels
                needs_validation = not has_all_required_labels or not all_above_threshold_or_optional
                logging.info(f'required labels: {_required_labels}')
                logging.info(f"existing labels: {_top_1_labels}")

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

    except Exception as e:
        logging.exception(e)

    if email_context := event.get('email'):
        subject = email_context.get('subject') or ''
        origin = email_context.get('origin') or ''
        header = f'{subject} (From: {origin})'
        output.update({
            'leadingTextHeader': {'value': header},
            'leadingText': {'value': email_context.get('body') or ''},
        })

    if metadata := event.get('metadata'):
        output['metadata'] = metadata

    logging.info(f'output: {output}')

    return {
        'documentId': document_id,
        'needsValidation': needs_validation,
        **output
    }
