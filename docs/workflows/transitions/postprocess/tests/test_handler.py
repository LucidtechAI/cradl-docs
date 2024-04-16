import pytest
import json
import base64
import runpy
import requests_mock

from unittest.mock import patch, ANY


@pytest.fixture
def field_config():
    yield base64.b64encode(json.dumps({
        'total_amount': {},
    }).encode('utf-8'))


@pytest.fixture
def env():
    yield {
        'TRANSITION_ID': 'xyz',
        'EXECUTION_ID': 'xyz',
        'DATASET_ID': 'las:dataset:xyz',
        'MODEL_ID': 'las:model:xyz',
    }


@pytest.fixture
def env_with_webhook_uri(env):
    yield {
        **env,
        'WEBHOOK_URI': 'https://foo.bar/',
    }


@pytest.fixture
def env_with_webhook_endpoints(env):
    yield {
        **env,
        'WEBHOOK_ENDPOINTS': '[{"uri": "https://foo.bar/"}, {"uri": "https://baz.bar/"}]'
    }


@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.update_document')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
def test_handler(get_document, get_asset, update_document, update_transition_excs, get_transition_excs, env):
    get_transition_excs.return_value = {
        'input': {
            'documentId': 'las:document:xyz',
            'needsValidation': False,
            'verified': {}
        }
    }

    with patch.dict('postprocess.feedback_and_export.os.environ', env):
        runpy.run_module('postprocess', run_name='__main__')


@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.update_document')
@patch('las.Client.get_document')
def test_webhook(get_document, update_document, update_transition_excs, get_transition_excs, env_with_webhook_uri):
    get_transition_excs.return_value = {
        'input': {
            'documentId': 'las:document:xyz',
            'needsValidation': True,
            'verified': {}
        }
    }

    with patch.dict('postprocess.feedback_and_export.os.environ', env_with_webhook_uri):
        with requests_mock.Mocker() as m:
            m.post(env_with_webhook_uri['WEBHOOK_URI'])
            runpy.run_module('postprocess', run_name='__main__')
            assert m.call_count == 1

            history = m.request_history[0]
            assert history.method == 'POST'
            assert history.url == env_with_webhook_uri['WEBHOOK_URI']

            for key in ['documentId', 'datasetId', 'values']:
                assert key in history.json()


@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.update_document')
@patch('las.Client.get_document')
def test_multiple_webhook_endpoints(
    get_document, update_document, update_transition_excs,
    get_transition_excs, env_with_webhook_endpoints
):
    get_transition_excs.return_value = {
        'input': {
            'documentId': 'las:document:xyz',
            'needsValidation': True,
            'verified': {}
        }
    }

    with patch.dict('postprocess.feedback_and_export.os.environ', env_with_webhook_endpoints):
        with requests_mock.Mocker() as m:
            endpoints = json.loads(env_with_webhook_endpoints['WEBHOOK_ENDPOINTS'])
            for endpoint in endpoints:
                m.post(endpoint['uri'])

            runpy.run_module('postprocess', run_name='__main__')
            assert m.call_count == len(endpoints)

            history = m.request_history[0]
            assert history.method == 'POST'
            assert history.url == endpoints[0]['uri']

            for key in ['documentId', 'datasetId', 'values']:
                assert key in history.json()


@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.update_document')
@patch('las.Client.get_document')
def test_update_ground_truth(get_document, update_document, update_transition_excs, get_transition_excs, env):
    get_transition_excs.return_value = {
        'input': {
            'documentId': 'las:document:xyz',
            'verified': {
                'foo': 'bar',
            }
        }
    }

    get_document.return_value = {'groundTruth': [{'label': 'baz', 'value': 'foobar'}]}

    with patch.dict('postprocess.feedback_and_export.os.environ', env):
        runpy.run_module('postprocess', run_name='__main__')

    update_document.assert_called_with(
        document_id='las:document:xyz',
        ground_truth=[{
            'label': 'baz',
            'value': 'foobar'
        }, {
            'label': 'foo',
            'value': 'bar'
        }],
        dataset_id='las:dataset:xyz'
    )


@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.update_document')
@patch('las.Client.get_document')
def test_update_ground_truth_with_lines(
    get_document, update_document, update_transition_excs, get_transition_excs, env
):
    get_transition_excs.return_value = {
        'input': {
            'documentId': 'las:document:xyz',
            'needsValidation': True,
            'verified': {
                'foo': 'bar',
                'line_items': [
                    {
                        'description': 'description_line_1',
                        'total_price': '1.00'
                    },
                    {
                        'description': 'description_line_2',
                        'total_price': '2.00'
                    },
                    {
                        'description': 'description_line_3',
                        'total_price': '3.00'
                    }
                ],
                'purchase_date': '2023-09-21',
            }
        }
    }

    get_document.return_value = {'groundTruth': [
        {'label': 'baz', 'value': 'foobar'},
        {'label': 'line_items_1', 'value': [
            [{'label': 'prod', 'value': 'abc'}, {'label': 'unit_price', 'value': '10.00'}],
            [{'label': 'prod', 'value': 'def'}, {'label': 'unit_price', 'value': '20.00'}]]}
    ]}

    with patch.dict('postprocess.feedback_and_export.os.environ', env):
        runpy.run_module('postprocess', run_name='__main__')

    update_document.assert_called_with(
        document_id='las:document:xyz',
        ground_truth=[{
            'label': 'baz',
            'value': 'foobar'
        }, {
            'label': 'line_items_1',
            'value': [
                [
                    {'label': 'prod', 'value': 'abc'},
                    {'label': 'unit_price', 'value': '10.00'}
                ],
                [
                    {'label': 'prod', 'value': 'def'},
                    {'label': 'unit_price', 'value': '20.00'}
                ]
            ]
        }, {
            'label': 'foo',
            'value': 'bar'
        }, {
            'label': 'line_items',
            'value': [
                [
                    {'label': 'description', 'value': 'description_line_1'},
                    {'label': 'total_price', 'value': '1.00'}
                ],
                [
                    {'label': 'description', 'value': 'description_line_2'},
                    {'label': 'total_price', 'value': '2.00'}
                ],
                [
                    {'label': 'description', 'value': 'description_line_3'},
                    {'label': 'total_price', 'value': '3.00'}
                ]
            ]
        }, {
            'label': 'purchase_date',
            'value': '2023-09-21'
        }],
        dataset_id='las:dataset:xyz'
    )


@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.update_document')
@patch('las.Client.get_document')
def test_update_ground_truth_with_same_lines(
    get_document, update_document, update_transition_excs, get_transition_excs, env
):
    get_transition_excs.return_value = {
        'input': {
            'documentId': 'las:document:xyz',
            'needsValidation': True,
            'verified': {
                'foo': 'bar',
                'line_items': [
                    {
                        'description': 'description_line_1',
                        'total_price': '1.00'
                    },
                    {
                        'description': 'description_line_2',
                        'total_price': '2.00'
                    },
                    {
                        'description': 'description_line_3',
                        'total_price': '3.00'
                    }
                ],
                'purchase_date': '2023-09-21',
            }
        }
    }

    get_document.return_value = {'groundTruth': [
        {'label': 'baz', 'value': 'foobar'},
        {'label': 'line_items', 'value': [
            [{'label': 'description', 'value': 'abc'}, {'label': 'total_price', 'value': '10.00'}],
            [{'label': 'description', 'value': 'def'}, {'label': 'total_price', 'value': '20.00'}]]}
    ]}

    with patch.dict('postprocess.feedback_and_export.os.environ', env):
        runpy.run_module('postprocess', run_name='__main__')

    update_document.assert_called_with(
        document_id='las:document:xyz',
        ground_truth=[{
            'label': 'baz',
            'value': 'foobar'
        }, {
            'label': 'line_items',
            'value': [
                [
                    {'label': 'description', 'value': 'description_line_1'},
                    {'label': 'total_price', 'value': '1.00'}
                ],
                [
                    {'label': 'description', 'value': 'description_line_2'},
                    {'label': 'total_price', 'value': '2.00'}
                ],
                [
                    {'label': 'description', 'value': 'description_line_3'},
                    {'label': 'total_price', 'value': '3.00'}
                ]
            ]
        }, {
            'label': 'foo',
            'value': 'bar'
        }, {
            'label': 'purchase_date',
            'value': '2023-09-21'
        }],
        dataset_id='las:dataset:xyz'
    )


@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.update_document')
@patch('las.Client.get_document')
def test_update_ground_truth_with_empty_lines(
    get_document, update_document, update_transition_excs, get_transition_excs, env
):
    get_transition_excs.return_value = {
        'input': {
            'documentId': 'las:document:xyz',
            'needsValidation': True,
            'verified': {
                'foo': 'bar',
                'line_items': [],
                'purchase_date': '2023-09-21',
                'string_value': '',
            }
        }
    }

    get_document.return_value = {'groundTruth': [
        {'label': 'baz', 'value': 'foobar'},
    ]}

    with patch.dict('postprocess.feedback_and_export.os.environ', env):
        runpy.run_module('postprocess', run_name='__main__')

    update_document.assert_called_with(
        document_id='las:document:xyz',
        ground_truth=[{
            'label': 'baz',
            'value': 'foobar',
        }, {
            'label': 'foo',
            'value': 'bar',
        }, {
            'label': 'purchase_date',
            'value': '2023-09-21',
        }, {
            'label': 'string_value',
            'value': '',
        }],
        dataset_id='las:dataset:xyz'
    )


@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.update_document')
@patch('las.Client.get_document')
def test_post_feedback_v2(get_document, update_document, update_transition_excs, get_transition_excs, env):
    validated_predictions = {
        'totalAmount': {"value": "100.00", "pages": [0, 1], "confidence": 1.0},
        'line_items': [{
            "unitPrice": {"value": "50.00", "pages": [0], "confidence": 0.8},
            "totalPrice": {"value": "100.00", "pages": [0], "confidence": 0.9}
        }, {
            "unitPrice": {"value": "50.00", "pages": [0], "confidence": 0.8},
            "totalPrice": {"value": "100.00", "pages": [0], "confidence": 0.9}
        }]
    }

    get_transition_excs.return_value = {
        'input': {
            'documentId': 'las:document:xyz',
            'validatedPredictions': validated_predictions
        }
    }

    get_document.return_value = {'groundTruth': [{'label': 'baz', 'value': 'foobar'}]}

    with patch.dict('postprocess.feedback_and_export.os.environ', env):
        runpy.run_module('postprocess', run_name='__main__')

    update_document.assert_called_with(
        document_id='las:document:xyz',
        ground_truth=ANY,
        dataset_id='las:dataset:xyz'
    )
