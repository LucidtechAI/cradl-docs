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


def convert_predictions_to_v2(predictions, field_config):
    if not predictions:
        return {}

    result = collections.defaultdict(list)
    for p in predictions:
        label, value = p['label'], p['value']
        config = field_config.get(label)
        if not config:
            logging.info(f'Could not find entry for label {label} in fieldConfig, skipping...')
            continue

        if config['type'] == 'lines':
            result[label] = [convert_predictions_to_v2(line, config.get('fields', {})) for line in value]
        else:
            result[label] += [{k: p[k] for k in p.keys() - {'label'}}]
            result[label] = sorted(result[label], key=lambda p: -p['confidence'])

    return result


def to_validated_format(predictions_v2, field_config):
    validated_format = {}

    def to_validated(v):
        return {'isEdited': False, 'automated': True, **v}

    def to_top1_or_multivalue(v, multivalue):
        if multivalue:
            return [to_validated(_v) for _v in v]
        elif len(v):
            return to_validated(v[0])
        return {}

    for field, val in predictions_v2.items():
        config = field_config.get(field)
        if not config:
            logging.info(f'Could not find entry for label {field} in fieldConfig, skipping...')
            continue
        is_multivalue = config.get('isMultivalue', False)

        if config['type'] == 'lines':
            validated_format[field] = [to_validated_format(line, config.get('fields', {})) for line in val]
        elif val:
            validated_format[field] = to_top1_or_multivalue(val, is_multivalue)

    return validated_format
