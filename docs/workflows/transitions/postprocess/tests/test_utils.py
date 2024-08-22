import pytest

from postprocess.utils import convert_predictions_to_v2, to_validated_format


@pytest.fixture
def v1_preds():
    yield [{
        'label': 'total_amount',
        'value': '150.00',
        'confidence': 0.9523123,
        'page': 2
    }, {
        'label': 'invoice_id',
        'value': '12345',
        'confidence': 0.9023123,
        'page': 0
    }, {
        'label': 'invoice_id',
        'value': '54321',
        'confidence': 0.9923123,
        'page': 0
    }, {
        'label': 'total_amount',
        'value': '150.00',
        'confidence': 0.85,
        'page': 1
    }, {
        'label': 'line_items',
        'value': [
            [{
                'label': 'line_amount',
                'value': '150.00',
                'confidence': 0.8,
                'page': 0
            }, {
                'label': 'description',
                'value': 'Foobar',
                'confidence': 0.8,
                'page': 1
            }, {
                'label': 'line_amount',
                'value': '350.00',
                'confidence': 0.95,
                'page': 0
            }],
            [{
                'label': 'line_amount',
                'value': '250.00',
                'confidence': 0.9,
                'page': 0

            }, {
                'label': 'description',
                'value': 'Bazbar',
                'confidence': 0.9,
                'page': 1
            }]
        ]
    }]


@pytest.fixture
def v2_preds():
    yield {
        'total_amount': [{
            'value': '120.00',
            'confidence': 0.9581
        }],
        'multivalue_field': [{
            'value': 'value1',
            'confidence': 0.8,
        }, {
            'value': 'value2',
            'confidence': 0.7,
        }],
        'line_items': [
            {
                'line_amount': [
                    {'value': '100.00', 'confidence': 0.99},
                    {'value': '50.00', 'confidence': 0.88}
                ],
                'description': [
                    {'value': 'Foo', 'confidence': 0.891},
                    {'value': 'Fooz', 'confidence': 0.5}
                ],
                'multivalue_col': [
                    {'value': 'value1', 'confidence': 0.8},
                    {'value': 'value2', 'confidence': 0.6}
                ],
            },
            {
                'line_amount': [
                    {'value': '200.00', 'confidence': 0.99},
                    {'value': '250.00', 'confidence': 0.88}
                ],
                'description': [
                    {'value': '130.00', 'confidence': 0.99},
                    {'value': '520.00', 'confidence': 0.88}
                ],
                'multivalue_col': [
                    {'value': 'value1', 'confidence': 0.8},
                    {'value': 'value2', 'confidence': 0.6}
                ],
            }
        ]
    }


def test_prediction_conversion(v1_preds, model):
    v2_preds = convert_predictions_to_v2(v1_preds, model['fieldConfig'])

    expected_keys = {'value', 'confidence', 'page'}

    assert len(v2_preds['total_amount']) == 2
    assert set(v2_preds['total_amount'][0].keys()) == expected_keys

    assert v2_preds['invoice_id'][0]['value'] == '54321'
    assert set(v2_preds['line_items'][0]['line_amount'][0].keys()) == expected_keys
    assert v2_preds['line_items'][0]['line_amount'][0]['value'] == '350.00'


def test_to_validated_format(v2_preds, model):
    validated = to_validated_format(v2_preds, model['fieldConfig'])

    assert validated['total_amount']['value'] == v2_preds['total_amount'][0]['value']
    assert len(validated['multivalue_field']) == 2
    assert validated['multivalue_field'][0]['value'] == v2_preds['multivalue_field'][0]['value']
    assert validated['multivalue_field'][1]['value'] == v2_preds['multivalue_field'][1]['value']
    line_0_val = validated['line_items'][0]
    line_0_pred = v2_preds['line_items'][0]
    assert line_0_val['line_amount']['value'] == line_0_pred['line_amount'][0]['value']
    assert line_0_val['description']['value'] == line_0_pred['description'][0]['value']
    assert len(line_0_val['multivalue_col']) == 2
    assert line_0_val['multivalue_col'][0]['value'] == line_0_pred['multivalue_col'][0]['value']
    assert line_0_val['multivalue_col'][1]['value'] == line_0_pred['multivalue_col'][1]['value']
    line_1_val = validated['line_items'][1]
    line_1_pred = v2_preds['line_items'][1]
    assert line_1_val['line_amount']['value'] == line_1_pred['line_amount'][0]['value']
    assert line_1_val['description']['value'] == line_1_pred['description'][0]['value']
    assert len(line_1_val['multivalue_col']) == 2
    assert line_1_val['multivalue_col'][0]['value'] == line_1_pred['multivalue_col'][0]['value']
    assert line_1_val['multivalue_col'][1]['value'] == line_1_pred['multivalue_col'][1]['value']
