import pytest
import preprocess
import las
import json
import base64
import runpy

from unittest.mock import patch


@pytest.fixture
def env():
    yield {
        'TRANSITION_ID': 'xyz',
        'EXECUTION_ID': 'xyz',
        'MODEL_ID': 'las:model:xyz',
        'FIELD_CONFIG_ASSET_ID': 'las:asset:xyz'
    }


@pytest.fixture
def field_config():
    yield base64.b64encode(json.dumps({
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
    }).encode('utf-8'))
    

@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
def test_run_module(get_asset, update_excs, get_excs, create_pred, field_config, env):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_asset.return_value = {'content': field_config}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        runpy.run_module(preprocess.__name__)
        

@pytest.mark.parametrize('prediction', [[
    # One field below threshold
    {'label': 'total_amount', 'confidence': 0.99},
    {'label': 'due_date',     'confidence': 0.97},
    {'label': 'invoice_id',   'confidence': 0.98},
], [
    # Missing required field, but all existing fields above threshold
    {'label': 'total_amount', 'confidence': 0.99},
    {'label': 'invoice_id',     'confidence': 0.99},
]])
@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
def test_low_confidence_predictions(
    get_asset, update_excs, get_excs, create_pred,
    field_config, prediction, env
):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_asset.return_value = {'content': field_config}
    create_pred.return_value = {'predictions': prediction}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()
        
    output = update_excs.call_args.kwargs['output']
    assert output['needsValidation'] == True
    

@pytest.mark.parametrize('prediction', [[
    # All above threshold
    {'label': 'total_amount', 'value': '123.00', 'confidence': 0.99},
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
def test_high_confidence_predictions(
    get_asset, update_excs, get_excs, create_pred,
    field_config, prediction, env
):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_asset.return_value = {'content': field_config}
    create_pred.return_value = {'predictions': prediction}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()
        
    output = update_excs.call_args.kwargs['output']
    assert output['needsValidation'] == False
    assert output['verified']
    