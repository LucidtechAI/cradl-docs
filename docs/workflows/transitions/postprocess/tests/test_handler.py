import pytest
import postprocess
import las
import json
import base64
import runpy

import requests_mock
from unittest.mock import patch


@pytest.fixture
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.update_document')
@patch('las.Client.get_asset')
def test_handler(get_asset, update_document, update_transition_excs, get_transition_excs):
    env = {
        'TRANSITION_ID': 'xyz',
        'EXECUTION_ID': 'xyz',
        'MODEL_ID': 'las:model:xyz',
    }
    
    get_transition_excs.return_value = {
        'input': {
            'documentId': 'las:document:xyz',
            'verified': {}
        }
    }

    with patch.dict('postprocess.feedback_and_export.os.environ', env):
        runpy.run_module(postprocess.__name__)
        

@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.update_document')
def test_webhook(update_document, update_transition_excs, get_transition_excs):
    env = {
        'TRANSITION_ID': 'xyz',
        'EXECUTION_ID': 'xyz',
        'MODEL_ID': 'las:model:xyz',
        'WEBHOOK_URI': 'https://foo.bar/webhook'
    }
    
    get_transition_excs.return_value = {
        'input': {
            'documentId': 'las:document:xyz',
            'verified': {}
        }
    }

    with patch.dict('postprocess.feedback_and_export.os.environ', env):
        with requests_mock.Mocker() as m:
            m.post(env['WEBHOOK_URI'])
            runpy.run_module(postprocess.__name__)
            assert m.call_count == 1
            
            history = m.request_history[0]
            assert history.method == 'POST'
            assert history.url == env['WEBHOOK_URI']

            for key in ['documentId', 'datasetId', 'values']:
                assert key in history.json()