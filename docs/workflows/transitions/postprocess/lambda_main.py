import os

from postprocess.feedback_and_export import feedback_and_export

CUSTOMER_ENVIRONMENT_VARIABLES = [
    'DATASET_ID',
    'MODEL_ID',
    'WEBHOOK_ENDPOINTS',
    'WEBHOOK_URI',
]


def main(lambda_event, _):
    for key in CUSTOMER_ENVIRONMENT_VARIABLES:
        os.environ.pop(key, None)

    for environment_variable in lambda_event:
        os.environ[environment_variable['name']] = environment_variable['value']
    feedback_and_export()
