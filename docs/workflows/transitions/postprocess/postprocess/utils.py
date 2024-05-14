import collections
import json
import logging


def parse_webhook_endpoints(s):
    if not s:
        return []

    try:
        webhook_endpoints = json.loads(s)
        if isinstance(webhook_endpoints, list):
            return webhook_endpoints
        else:
            print('Ignoring WEBHOOK_ENDPOINTS. It must be a JSON list, not dict.')
            return []
    except json.JSONDecodeError as e:
        logging.error(f'Unable to JSON decode webhook endpoints: {e}')

    return []


def convert_predictions_to_v2(predictions):
    if not predictions:
        return {}

    result = collections.defaultdict(list)
    for p in predictions:
        label, value = p['label'], p['value']

        if isinstance(value, list):
            result[label] = [convert_predictions_to_v2(line) for line in value]
        else:
            result[label] += [{k: p[k] for k in p.keys() - {'label'}}]
            result[label] = sorted(result[label], key=lambda p: -p['confidence'])

    return result


def to_validated_format(predictions_v2):
    def top1_pred(val):
        if not all([isinstance(v, list) for v in val[0].values()]):
            return {'isEdited': False, 'automated': True, **val[0]}

        return [to_validated_format(line) for line in val]

    return {field: top1_pred(val) for field, val in predictions_v2.items()}
