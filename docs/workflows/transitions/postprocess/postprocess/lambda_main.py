from .feedback_and_export import feedback_and_export


def main(lambda_event, _):
    for key, value in lambda_event.items():
        os.environ[key] = value
    feedback_and_export()