import pytest
import preprocess
import las
import json
import base64
import runpy

from unittest.mock import patch, MagicMock

from preprocess.utils import (
    filter_by_top1,
    merge_lines_from_different_pages,
    patch_empty_predictions,
    get_labels,
    get_column_names,
    filter_away_low_confidence_lines,
)


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
                },
                'currency': {
                    'type': 'enum',
                    'confidenceLevels': {'automated': 0.98, 'high': 0.97, 'medium': 0.9, 'low': 0.5},
                },
                'line_items': {
                    'type': 'lines',
                    'fields': {
                        'subtotal': {
                            'type': 'string',
                            'confidenceLevels': {'automated': 0.98, 'high': 0.97, 'medium': 0.9, 'low': 0.5},
                        }
                    }
                }
            }
        }
    }).encode('utf-8'))


@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
@patch('las.Client.get_model')
def test_run_module(get_model, get_document, get_asset, update_excs, get_excs, create_pred, form_config, env):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_model.return_value = {'metadata': {}}
    get_document.return_value = MagicMock()
    get_asset.return_value = {'content': form_config}
    create_pred.return_value = {'next_page': None}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        runpy.run_module(preprocess.__name__)


@pytest.mark.parametrize('predictions', [[
    {'label': 'total_amount', 'value': '1', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1', 'confidence': 0.80},
    {'label': 'invoice_id', 'value': '1', 'confidence': 0.98},
]])
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
@patch('las.Client.get_model')
def test_override_predictions(
    get_model, get_document, get_asset, update_excs, get_excs, form_config, predictions, env
):
    get_excs.return_value = {'input': {
        'documentId': 'las:document:xyz',
        'predictions': predictions
    }}
    get_model.return_value = {'metadata': {}}
    get_document.return_value = MagicMock()
    get_asset.return_value = {'content': form_config}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()
        
    output = update_excs.call_args.kwargs['output']
    assert output['needsValidation'] == True


@pytest.mark.parametrize('prediction', [[
    # One field below threshold
    {'label': 'total_amount', 'value': '1', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1', 'confidence': 0.80},
    {'label': 'invoice_id', 'value': '1', 'confidence': 0.98},
    {'label': 'currency', 'value': '1', 'confidence': 0.99},
    {'label': 'line_items', 'type': 'lines', 'value': [
        [{'label': 'subtotal', 'value': '50.00', 'confidence': 0.99}]
    ]},
], [
    # Missing required field, but all existing fields above threshold
    {'label': 'total_amount', 'value': '1', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '1', 'confidence': 0.99},
], [
    # One required field missing
    {'label': 'total_amount', 'value': '1', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '1', 'confidence': 0.99},
    {'label': 'random', 'value': 'foobar', 'confidence': 0.99},
    {'label': 'currency', 'value': '1', 'confidence': 0.99},
], [
    # Line label below threshold
    {'label': 'total_amount', 'value': '1', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '1', 'confidence': 0.99},
    {'label': 'currency', 'value': '1', 'confidence': 0.99},
    {'label': 'line_items', 'type': 'lines', 'value': [
        [{'label': 'subtotal', 'value': '50.00', 'confidence': 0.1}]
    ]},
], [
    # Line label empty
    {'label': 'total_amount', 'value': '1', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '1', 'confidence': 0.99},
    {'label': 'currency', 'value': '1', 'confidence': 0.99},
    {'label': 'line_items', 'type': 'lines', 'value': [[]]},
]])
@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
@patch('las.Client.get_model')
def test_low_confidence_predictions(
    get_model, get_document, get_asset, update_excs, get_excs, create_pred, form_config, prediction, env
):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_model.return_value = {'metadata': {}}
    get_document.return_value = MagicMock()
    get_asset.return_value = {'content': form_config}
    create_pred.return_value = {'predictions': prediction}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()
        
    output = update_excs.call_args.kwargs['output']
    assert output['needsValidation']
    

@pytest.mark.parametrize('predictions', [[
    # All above threshold
    {'label': 'total_amount', 'value': '123.00', 'confidence': 0.99},
    {'label': 'due_date', 'value': '2022-05-17', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '0665', 'confidence': 0.99},
    {'label': 'currency', 'value': 'NOK', 'confidence': 0.99},
    {'label': 'line_items', 'type': 'lines', 'value': [
        [{'label': 'subtotal', 'value': '50.00', 'confidence': 0.99}]
    ]},
], [
    # All top-1 above threshold
    {'label': 'total_amount', 'value': '123.00', 'confidence': 0.99},
    {'label': 'total_amount', 'value': '123.00', 'confidence': 0.1},
    {'label': 'due_date', 'value': '2022-05-17', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '0665', 'confidence': 0.99},
    {'label': 'currency', 'value': 'NOK', 'confidence': 0.99},
    {'label': 'currency', 'value': 'SEK', 'confidence': 0.2},
    {'label': 'line_items', 'type': 'lines', 'value': [
        [{'label': 'subtotal', 'value': '50.00', 'confidence': 0.99}]
    ]},
], [
    # All required above threshold, optional below lower threshold + random field not present in field config
    {'label': 'total_amount', 'value': '0.00', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1991-08-02', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '1337', 'confidence': 0.05},
    {'label': 'currency', 'value': 'NOK', 'confidence': 0.99},
    {'label': 'line_items', 'type': 'lines', 'value': [
        [{'label': 'subtotal', 'value': '50.00', 'confidence': 0.99}]
    ]},
], [
    # All required above threshold
    {'label': 'total_amount', 'value': '0.00', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1991-07-25', 'confidence': 0.99},
    {'label': 'currency', 'value': 'NOK', 'confidence': 0.99},
    {'label': 'line_items', 'type': 'lines', 'value': [
        [{'label': 'subtotal', 'value': '50.00', 'confidence': 0.99}]
    ]},
]])
@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
@patch('las.Client.get_model')
def test_high_confidence_predictions(
    get_model, get_document, get_asset, update_excs, get_excs, create_pred, form_config, predictions, env
):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_model.return_value = {'metadata': {}}
    get_document.return_value = MagicMock()
    get_asset.return_value = {'content': form_config}
    create_pred.return_value = {'predictions': predictions}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()
        
    output = update_excs.call_args.kwargs['output']

    assert not output['needsValidation']
    assert output['verified']
    

@pytest.mark.parametrize('predictions', [[
    # All required above threshold, optional below lower threshold
    {'label': 'total_amount', 'value': '0.00', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1991-08-02', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '1337', 'confidence': 0.05},
    {'label': 'currency', 'value': 'NOK', 'confidence': 0.99},
    {'label': 'line_items', 'value': [[{'label': 'subtotal', 'value': '10.00', 'confidence': 0.98}]]},
]])
@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
@patch('las.Client.get_model')
def test_low_confidence_and_optional_fields_are_omitted(
    get_model, get_document, get_asset, update_excs, get_excs, create_pred, form_config, predictions, env
):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_model.return_value = {'metadata': {}}
    get_document.return_value = MagicMock()
    get_asset.return_value = {'content': form_config}
    create_pred.return_value = {'predictions': predictions}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()

    output = update_excs.call_args.kwargs['output']
    assert 'invoice_id' not in output['verified']


@pytest.mark.parametrize('predictions', [[
    # All required above threshold, optional below lower threshold
    {'label': 'total_amount', 'value': '0.00', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1991-08-02', 'confidence': 0.99},
    {'label': 'invoice_id', 'value': '1337', 'confidence': 0.05},
    {'label': 'currency', 'value': None, 'confidence': 0.99},
    {'label': 'currency', 'value': 'EUR', 'confidence': 0.5},
    {'label': 'line_items', 'value': [[{'label': 'subtotal', 'value': '10.00', 'confidence': 0.98}]]},
]])
@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
@patch('las.Client.get_model')
def test_enum_null_values_sent_to_need_validation(
    get_model, get_document, get_asset, update_excs, get_excs, create_pred, form_config, predictions, env
):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_model.return_value = {'metadata': {}}
    get_document.return_value = MagicMock()
    get_asset.return_value = {'content': form_config}
    create_pred.return_value = {'predictions': predictions}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()

    output = update_excs.call_args.kwargs['output']
    assert output['needsValidation']


@pytest.mark.parametrize('predictions', [[
    {'label': 'total_amount', 'value': '0.00', 'confidence': 0.99},
    {'label': 'due_date', 'value': '1991-08-02', 'confidence': 0.99},
    {'label': 'line_items', 'value': [[{'label': 'subtotal', 'value': '10.00', 'confidence': 0.8}]]},
]])
@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
@patch('las.Client.get_model')
def test_update_ground_truth_values(
    get_model, get_document, get_asset, update_excs, get_excs, create_pred, form_config, predictions, env
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
    get_model.return_value = {'metadata': {}}
    get_document.return_value = {'groundTruth': ground_truth}
    get_asset.return_value = {'content': form_config}
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


@pytest.mark.parametrize('predictions', [[
    {'label': 'due_date', 'value': '1991-08-02', 'confidence': 0.99},
    {'label': 'total_amount', 'value': '0.00', 'confidence': 0.99},
    {'label': 'line_items', 'value': [[{'label': 'subtotal', 'value': '10.00', 'confidence': 0.8}]]},
]])
@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
@patch('las.Client.get_model')
def test_update_ground_truth_values_no_lines(
    get_model, get_document, get_asset, update_excs, get_excs, create_pred, form_config, predictions, env
):
    ground_truth = [
        {'label': 'total_amount', 'value': '100.00'},
    ]
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_model.return_value = {'metadata': {}}
    get_document.return_value = {'groundTruth': ground_truth}
    get_asset.return_value = {'content': form_config}
    create_pred.return_value = {'predictions': predictions}

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()

    output = update_excs.call_args.kwargs['output']

    gt_labels = [gt['label'] for gt in ground_truth]
    assert output['needsValidation']
    for count, prediction in enumerate(output['predictions']):
        if prediction['label'] in gt_labels:
            assert prediction['confidence'] == 1.0
        else:
            assert prediction == predictions[count]


@patch('las.Client.create_prediction')
@patch('las.Client.get_transition_execution')
@patch('las.Client.update_transition_execution')
@patch('las.Client.get_asset')
@patch('las.Client.get_document')
@patch('las.Client.get_model')
def test_inactive_model(
    get_model, get_document, get_asset, update_excs, get_excs, create_pred, form_config, env
):
    get_excs.return_value = {'input': {'documentId': 'las:document:xyz'}}
    get_model.return_value = {'metadata': {}}
    get_document.return_value = MagicMock()
    get_asset.return_value = {'content': form_config}
    
    def side_effect(*args, **kwargs):
        raise las.client.BadRequest('Some bad request')

    create_pred.side_effect = side_effect

    with patch.dict('preprocess.make_predictions.os.environ', env):
        preprocess.make_predictions.make_predictions()
        
    output = update_excs.call_args.kwargs['output']
    assert output['needsValidation'] == True


@pytest.fixture
def predictions_to_collapse():
    return [
        {'label': 'total_amount', 'value': '500', 'confidence': 0.99},
        {'label': 'total_amount', 'value': '300', 'confidence': 0.90},
        {'label': 'line_items', 'value': [
            [
                {'label': 'subtotal', 'value': '100', 'confidence': 0.98},
                {'label': 'subtotal', 'value': '200', 'confidence': 0.95},
            ],
            [
                {'label': 'subtotal', 'value': '300', 'confidence': 0.95}
            ]
        ]},
    ]


@pytest.fixture
def expected_collapsed_predictions():
    return [
        {'label': 'total_amount', 'value': '500', 'confidence': 0.99},
        {'label': 'line_items', 'value': [
            [
                {'label': 'subtotal', 'value': '100', 'confidence': 0.98},
            ],
            [
                {'label': 'subtotal', 'value': '300', 'confidence': 0.95}
            ]
        ]},
    ]


def test_top1_filter(predictions_to_collapse, expected_collapsed_predictions, form_config):
    form_config = json.loads(base64.b64decode(form_config))
    form_config = form_config['config']['fields']
    labels = get_labels(form_config)
    column_names = get_column_names(form_config)
    labels = labels.union(column_names)

    filtered_predictions = filter_by_top1(predictions_to_collapse, labels)
    filtered_predictions = sorted(filtered_predictions, key=lambda item: item['label'])
    expected_filtered_predictions = sorted(expected_collapsed_predictions, key=lambda item: item['label'])

    assert filtered_predictions == expected_filtered_predictions


@pytest.fixture
def line_predictions_to_merge():
    return [
        {'label': 'supplier_name', 'page': 0, 'value': 'One cool supplier', 'confidence': 0.90},
        {'label': 'supplier_name', 'page': 0, 'value': 'Not a supplier', 'confidence': 0.88},
        {'label': 'line_items', 'value': [
            [
                {'label': 'description', 'page': 0, 'value': 'first line', 'confidence': 0.93},
                {'label': 'product_code', 'page': 0, 'value': None, 'confidence': 0.65},
                {'label': 'unit_price', 'page': 0, 'value': '10.00', 'confidence': 0.38},
            ], [
                {'label': 'description', 'page': 0, 'value': 'second line', 'confidence': 0.95},
                {'label': 'product_code', 'page': 0, 'value': None, 'confidence': 0.65},
                {'label': 'total_price', 'page': 0, 'value': '3691.95', 'confidence': 0.65},
                {'label': 'unit_price', 'page': 0, 'value': '11.00', 'confidence': 0.38},
                {'label': 'total_price', 'page': 0, 'value': '3.691.95', 'confidence': 0.36},
            ], [
                {'label': 'description', 'page': 0, 'value': 'third line', 'confidence': 0.94},
                {'label': 'total_price', 'page': 0, 'value': '188.57', 'confidence': 0.40},
            ]
        ]},
        {'label': 'supplier_name', 'page': 1, 'value': None, 'confidence': 0.89},
        {'label': 'line_items', 'value': [
            [
                {'label': 'description', 'page': 1, 'value': 'third line', 'confidence': 0.96},
                {'label': 'description', 'page': 1, 'value': 'thir line', 'confidence': 0.36},
                {'label': 'unit_price', 'page': 1, 'value': '10.11', 'confidence': 0.38},
                {'label': 'product_code', 'page': 1, 'value': 'ABC123', 'confidence': 0.65},
            ], [
                {'label': 'total_price', 'page': 1, 'value': '395.40', 'confidence': 0.92},
                {'label': 'description', 'page': 1, 'value': 'fourth line', 'confidence': 0.909},
            ], [
                {'label': 'total_price', 'page': 1, 'value': '23090.35', 'confidence': 0.60},
                {'label': 'description', 'page': 1, 'value': 'fifth line', 'confidence': 0.55},
                {'label': 'product_code', 'page': 1, 'value': 'fifth line', 'confidence': 0.302},
            ]
        ]},
        {'label': 'supplier_name', 'page': 2, 'value': 'One cool supplier', 'confidence': 0.84},
        {'label': 'line_items', 'value': [
            [
                {'label': 'total_price', 'page': 2, 'value': '72.15', 'confidence': 0.96},
                {'label': 'unit_price', 'page': 2, 'value': '62.05', 'confidence': 0.61},
                {'label': 'product_code', 'page': 2, 'value': None, 'confidence': 0.48},
            ], [
                {'label': 'total_price', 'page': 2, 'value': '51.82', 'confidence': 0.93},
                {'label': 'unit_price', 'page': 2, 'value': '48.95', 'confidence': 0.464},
            ],
            [
                {'label': 'description', 'page': 3, 'value': 'sixth line', 'confidence': 0.93},
                {'label': 'product_code', 'page': 3, 'value': None, 'confidence': 0.68},
            ],
        ]},
    ]


@pytest.fixture
def line_predictions_after_merge():
    return [
        {'label': 'supplier_name', 'page': 0, 'value': 'One cool supplier', 'confidence': 0.90},
        {'label': 'supplier_name', 'page': 0, 'value': 'Not a supplier', 'confidence': 0.88},
        {'label': 'supplier_name', 'page': 1, 'value': None, 'confidence': 0.89},
        {'label': 'supplier_name', 'page': 2, 'value': 'One cool supplier', 'confidence': 0.84},
        {'label': 'line_items', 'value': [
            [
                {'label': 'description', 'page': 0, 'value': 'first line', 'confidence': 0.93},
                {'label': 'product_code', 'page': 0, 'value': None, 'confidence': 0.65},
                {'label': 'unit_price', 'page': 0, 'value': '10.00', 'confidence': 0.38},
            ], [
                {'label': 'description', 'page': 0, 'value': 'second line', 'confidence': 0.95},
                {'label': 'product_code', 'page': 0, 'value': None, 'confidence': 0.65},
                {'label': 'total_price', 'page': 0, 'value': '3691.95', 'confidence': 0.65},
                {'label': 'unit_price', 'page': 0, 'value': '11.00', 'confidence': 0.38},
                {'label': 'total_price', 'page': 0, 'value': '3.691.95', 'confidence': 0.36},
            ], [
                {'label': 'description', 'page': 0, 'value': 'third line', 'confidence': 0.94},
                {'label': 'total_price', 'page': 0, 'value': '188.57', 'confidence': 0.40},
                {'label': 'description', 'page': 1, 'value': 'third line', 'confidence': 0.96},
                {'label': 'description', 'page': 1, 'value': 'thir line', 'confidence': 0.36},
                {'label': 'unit_price', 'page': 1, 'value': '10.11', 'confidence': 0.38},
                {'label': 'product_code', 'page': 1, 'value': 'ABC123', 'confidence': 0.65},
            ], [
                {'label': 'total_price', 'page': 1, 'value': '395.40', 'confidence': 0.92},
                {'label': 'description', 'page': 1, 'value': 'fourth line', 'confidence': 0.909},
            ], [
                {'label': 'total_price', 'page': 1, 'value': '23090.35', 'confidence': 0.60},
                {'label': 'description', 'page': 1, 'value': 'fifth line', 'confidence': 0.55},
                {'label': 'product_code', 'page': 1, 'value': 'fifth line', 'confidence': 0.302},
            ], [
                {'label': 'total_price', 'page': 2, 'value': '72.15', 'confidence': 0.96},
                {'label': 'unit_price', 'page': 2, 'value': '62.05', 'confidence': 0.61},
                {'label': 'product_code', 'page': 2, 'value': None, 'confidence': 0.48},
            ], [
                {'label': 'total_price', 'page': 2, 'value': '51.82', 'confidence': 0.93},
                {'label': 'unit_price', 'page': 2, 'value': '48.95', 'confidence': 0.464},
                {'label': 'description', 'page': 3, 'value': 'sixth line', 'confidence': 0.93},
                {'label': 'product_code', 'page': 3, 'value': None, 'confidence': 0.68},
            ],
        ]},
    ]


@pytest.fixture
def simple_field_config():
    return {
        'supplier_name': {'type': 'string'},
        'line_items': {
            'type': 'lines',
            'fields': {
                'description': {'type': 'string'},
                'total_price': {'type': 'amount'},
                'unit_price': {'type': 'amount'},
                'product_code': {'type': 'string'},
            }
        }
    }


def test_merge_lines_from_different_pages(simple_field_config, line_predictions_to_merge, line_predictions_after_merge):
    predictions = merge_lines_from_different_pages(line_predictions_to_merge, simple_field_config)
    assert predictions == line_predictions_after_merge


@pytest.mark.parametrize('predictions', [[
        {'label': 'supplier_name', 'page': 0, 'value': 'One cool supplier', 'confidence': 0.90},
        {'label': 'supplier_name', 'page': 0, 'value': 'Not a supplier', 'confidence': 0.88},
        {'label': 'supplier_name', 'page': 1, 'value': None, 'confidence': 0.95},
        {'label': 'supplier_name', 'page': 2, 'value': None, 'confidence': 0.84},
        {'label': 'total_amount', 'page': 0, 'value': '123.34', 'confidence': 0.56},
        {'label': 'total_amount', 'page': 1, 'value': None, 'confidence': 0.56},
        {'label': 'line_items', 'value': [
            [
                {'label': 'description', 'page': 0, 'value': 'first line', 'confidence': 0.93},
                {'label': 'product_code', 'page': 0, 'value': None, 'confidence': 0.65},
                {'label': 'unit_price', 'page': 0, 'value': '10.00', 'confidence': 0.38},
            ],
            [
                {'label': 'description', 'page': 1, 'value': 'second line', 'confidence': 0.96},
                {'label': 'unit_price', 'page': 1, 'value': '10.11', 'confidence': 0.38},
                {'label': 'product_code', 'page': 1, 'value': 'ABC123', 'confidence': 0.65},
            ],
        ]},
    ]])
@pytest.mark.parametrize('patched_predictions', [[
        {'label': 'supplier_name', 'page': 0, 'value': 'One cool supplier', 'confidence': 0.90},
        {'label': 'supplier_name', 'page': 0, 'value': 'Not a supplier', 'confidence': 0.88},
        {'label': 'total_amount', 'page': 0, 'value': '123.34', 'confidence': 0.56},
        {'label': 'line_items', 'value': [
            [
                {'label': 'description', 'page': 0, 'value': 'first line', 'confidence': 0.93},
                {'label': 'product_code', 'page': 0, 'value': None, 'confidence': 0.65},
                {'label': 'unit_price', 'page': 0, 'value': '10.00', 'confidence': 0.38},
            ],
            [
                {'label': 'description', 'page': 1, 'value': 'second line', 'confidence': 0.96},
                {'label': 'unit_price', 'page': 1, 'value': '10.11', 'confidence': 0.38},
                {'label': 'product_code', 'page': 1, 'value': 'ABC123', 'confidence': 0.65},
            ],
        ]},
        {'label': 'supplier_name', 'page': 2, 'value': None, 'confidence': 0.84},
    ]])
@pytest.mark.parametrize('no_empty_prediction_fields', [{'total_amount'}])
def test_patch_empty_predictions(predictions, patched_predictions, no_empty_prediction_fields):
    labels = ['supplier_name', 'total_amount', 'line_items']
    assert patch_empty_predictions(predictions, labels, no_empty_prediction_fields) == patched_predictions


@pytest.mark.parametrize('predictions', [[
    {'label': 'invoice_id', 'page': 0, 'value': '1234', 'confidence': 0.90},
    {'label': 'invoice_id', 'page': 0, 'value': '11234', 'confidence': 0.88},
    {'label': 'line_items', 'value': [
        [
            {'label': 'description', 'page': 0, 'value': 'first line', 'confidence': 0.93},
            {'label': 'product_code', 'page': 0, 'value': None, 'confidence': 0.65},
            {'label': 'unit_price', 'page': 0, 'value': '10.00', 'confidence': 0.38},
        ], [
            {'label': 'description', 'page': 0, 'value': 'second line', 'confidence': 0.2},
            {'label': 'total_price', 'page': 0, 'value': '3691.95', 'confidence': 0.2},
            {'label': 'unit_price', 'page': 0, 'value': '11.00', 'confidence': 0.3},
            {'label': 'total_price', 'page': 0, 'value': '3.691.95', 'confidence': 0.36},
        ], [],
    ]},
    {'label': 'invoice_id', 'page': 2, 'value': '5678', 'confidence': 0.84},
    {'label': 'line_items', 'value': [
        [
            {'label': 'total_price', 'page': 2, 'value': '72.15', 'confidence': 1.0},
        ],
        [
            {'label': 'total_price', 'page': 2, 'value': '72.15', 'confidence': 0.1},
            {'label': 'unit_price', 'page': 2, 'value': '62.05', 'confidence': 0.1},
            {'label': 'product_code', 'page': 2, 'value': None, 'confidence': 0.1},
        ],
    ]},
]])
@pytest.mark.parametrize('filtered_predictions', [[
    {'label': 'invoice_id', 'page': 0, 'value': '1234', 'confidence': 0.90},
    {'label': 'invoice_id', 'page': 0, 'value': '11234', 'confidence': 0.88},
    {'label': 'line_items', 'value': [
        [
            {'label': 'description', 'page': 0, 'value': 'first line', 'confidence': 0.93},
            {'label': 'product_code', 'page': 0, 'value': None, 'confidence': 0.65},
            {'label': 'unit_price', 'page': 0, 'value': '10.00', 'confidence': 0.38},
        ], [], [],
    ]},
    {'label': 'invoice_id', 'page': 2, 'value': '5678', 'confidence': 0.84},
    {'label': 'line_items', 'value': [[], []]},
]])
def test_filter_away_empty_lines(predictions, filtered_predictions, simple_field_config):
    assert filter_away_low_confidence_lines(predictions, simple_field_config) == filtered_predictions
