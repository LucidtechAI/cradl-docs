from .make_predictions import make_predictions

def main(lambda_event, _):
    for key, value in lambda_event.items():
        os.environ[key] = value
    make_predictions()