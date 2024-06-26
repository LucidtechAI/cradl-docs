import os

from preprocess.make_predictions import make_predictions


def main(lambda_event, _):
    for environment_variable in lambda_event:
        os.environ[environment_variable['name']] = environment_variable['value']
    make_predictions()
