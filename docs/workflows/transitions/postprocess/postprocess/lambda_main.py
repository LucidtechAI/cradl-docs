from .feedback_and_export import feedback_and_export


def main(lambda_event, _):
    for environment_variable in lambda_event:
        os.environ[environment_variable['name']] = environment_variable['value']
    feedback_and_export()