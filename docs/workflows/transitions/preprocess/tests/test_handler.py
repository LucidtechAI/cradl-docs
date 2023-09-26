import pytest
import preprocess
import las
import json
import base64
import runpy

from unittest.mock import patch, MagicMock


@pytest.fixture
def env():
    yield {
        'TRANSITION_ID': 'xyz',
        'EXECUTION_ID': 'xyz',
        'MODEL_ID': 'las:model:xyz',
        'FORM_CONFIG_ASSET_ID': 'las:asset:xyz'
    }


@pytest.fixture
def form_config():
    yield base64.b64encode(json.dumps({
        'config': {
            'fields': {
                'total_amount': {
                    'type': 'amount',
                    'confidenceLevels': {'automated': 0.98, 'high': 0.97, 'medium': 0.9, 'low': 0.5}
                },
                'due_date': {
                    'type': 'date',
                    'confidenceLevels': {'automated': 0.98, 'high': 0.97, 'medium': 0.9, 'low': 0.5}
                },
                'invoice_id': {
                    'type': 'string',
                    'confidenceLevels': {'automated': 0.98, 'high': 0.97, 'medium': 0.9, 'low': 0.5},
                    'required': False
                }
            }
        }
    }).encode('utf-8'))


@pytest.fixture
def form_config_with_lines():
    yield base64.b64encode(json.dumps({
        'config': {
            'fields': {
                'total_amount': {
                    'type': 'amount',
                    'confidenceLevels': {'automated': 0.98, 'high': 0.97, 'medium': 0.9, 'low': 0.5}
                },
                'due_date': {
                    'type': 'date',
                    'confidenceLevels': {'automated': 0.98, 'high': 0.97, 'medium': 0.9, 'low': 0.5}
                },
                'line_items': {
                    'type': 'lines',
                    'confidenceLevels': {'automated': 0.98, 'high': 0.97, 'medium': 0.9, 'low': 0.5},
                }
            }
        }
    }).encode('utf-8'))


@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
def test_run_module(get_document, get_asset, update_excs, get_excs, create_pred, form_config, env):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_document.return_value = MagicMock()
    get_asset.return_value = {'content': form_config}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        runpy.run_module(preprocess.__name__)
        

@pytest.mark.parametrize('prediction', [[
    # One field below threshold
    {'label': 'total_amount', 'value': '1', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1', 'confidence': 0.97},
    {'label': 'invoice_id', 'value': '1', 'confidence': 0.98},
], [
    # Missing required field, but all existing fields above threshold
    {'label': 'total_amount', 'value': '1', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '1', 'confidence': 0.99},
]])
@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
def test_low_confidence_predictions(
    get_document, get_asset, update_excs, get_excs, create_pred,
    form_config, prediction, env
):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_document.return_value = MagicMock()
    get_asset.return_value = {'content': form_config}
    create_pred.return_value = {'predictions': prediction}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()
        
    output = update_excs.call_args.kwargs['output']
    assert output['needsValidation'] == True
    

@pytest.mark.parametrize('predictions', [[
    # All above threshold
    {'label': 'total_amount', 'value': '123.00', 'confidence': 0.99},
    {'label': 'due_date', 'value': '2022-05-17', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '0665', 'confidence': 0.99},
], [
    # All top-1 above threshold
    {'label': 'total_amount', 'value': '123.00', 'confidence': 0.99},
    {'label': 'total_amount', 'value': '123.00', 'confidence': 0.1},
    {'label': 'due_date', 'value': '2022-05-17', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '0665', 'confidence': 0.99},
], [
    # All required above threshold
    {'label': 'total_amount', 'value': '1001.37', 'confidence': 0.99},
    {'label': 'due_date', 'value': '2022-07-25', 'confidence': 0.99},
], [
    # All required above threshold, optional below lower threshold
    {'label': 'total_amount', 'value': '0.00', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1991-08-02', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '1337', 'confidence': 0.05},
]])
@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
def test_high_confidence_predictions(
    get_document, get_asset, update_excs, get_excs, create_pred,
    form_config, predictions, env
):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_document.return_value = MagicMock()
    get_asset.return_value = {'content': form_config}
    create_pred.return_value = {'predictions': predictions}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()
        
    output = update_excs.call_args.kwargs['output']

    assert output['needsValidation'] == False
    assert output['verified']
    

@pytest.mark.parametrize('predictions', [[
    # All required above threshold, optional below lower threshold
    {'label': 'total_amount', 'value': '0.00', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1991-08-02', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '1337', 'confidence': 0.05},
]])
@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
def test_low_confidence_and_optional_fields_are_omitted(
    get_document, get_asset, update_excs, get_excs, create_pred,
    form_config, predictions, env
):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_document.return_value = MagicMock()
    get_asset.return_value = {'content': form_config}
    create_pred.return_value = {'predictions': predictions}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()

    output = update_excs.call_args.kwargs['output']
    assert 'invoice_id' not in output['verified']


@pytest.mark.parametrize('predictions', [[
    {'label': 'total_amount', 'value': '0.00', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1991-08-02', 'confidence': 0.99},
    {'label': 'line_items', 'value': [[{'label': 'total_price', 'value': '10.00', 'confidence': 0.8}]]},
]])
@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
def test_update_ground_truth_values(
    get_document, get_asset, update_excs, get_excs, create_pred,
    form_config_with_lines, predictions, env
):
    ground_truth = [
        {'label': 'total_amount', 'value': '100.00'},
        {'label': 'line_items', 'value': [[
                {'label': 'total_price', 'value': '10.00'}, {'label': 'description', 'value': 'line 1'},
            ],
            [
                {'label': 'total_price', 'value': '99.00'}, {'label': 'description', 'value': 'line 2'},
            ],
        ]}
    ]
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_document.return_value = {'groundTruth': ground_truth}
    get_asset.return_value = {'content': form_config_with_lines}
    create_pred.return_value = {'predictions': predictions}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()

    output = update_excs.call_args.kwargs['output']

    assert output['needsValidation']
    for prediction in output['predictions']:
        for gt in ground_truth:
            if prediction['label'] == gt['label']:
                assert prediction['value'] == gt['value']
                if isinstance(prediction['value'], list):
                    for line in prediction['value']:
                        assert [line_pred['confidence'] == 1.0 for line_pred in line]
                else:
                    assert prediction['confidence'] == 1.0
