import pytest

from postprocess.utils import convert_predictions_to_v2


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


def test_prediction_conversion(v1_preds):
    v2_preds = convert_predictions_to_v2(v1_preds)

    expected_keys = {'value', 'confidence', 'page'}

    assert len(v2_preds['total_amount']) == 2
    assert set(v2_preds['total_amount'][0].keys()) == expected_keys

    assert v2_preds['invoice_id'][0]['value'] == '54321'
    assert set(v2_preds['line_items'][0]['line_amount'][0].keys()) == expected_keys
    assert v2_preds['line_items'][0]['line_amount'][0]['value'] == '350.00'
