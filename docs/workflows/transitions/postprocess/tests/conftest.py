import pytest


@pytest.fixture
def model():
    return {
        'fieldConfig': {
            'total_amount': {
                'type': 'amount',
            },
            'invoice_id': {
                'type': 'string',
            },
            'multivalue_field': {
                'type': 'string',
                'isMultivalue': True,
            },
            'line_items': {
                'type': 'lines',
                'fields': {
                    'description': {
                        'type': 'string',
                    },
                    'line_amount': {
                        'type': 'amount',
                    },
                    'multivalue_col': {
                        'type': 'string',
                        'isMultivalue': True,
                    }
                },
            },
        },
    }
