import os

from postprocess.feedback_and_export import feedback_and_export


COMMON_ENV = [
    'AWS_ACCESS_KEY_ID',
    'AWS_DEFAULT_REGION',
    'AWS_EXECUTION_ENV',
    'AWS_LAMBDA_FUNCTION_MEMORY_SIZE',
    'AWS_LAMBDA_FUNCTION_NAME',
    'AWS_LAMBDA_FUNCTION_VERSION',
    'AWS_LAMBDA_INITIALIZATION_TYPE',
    'AWS_LAMBDA_LOG_GROUP_NAME',
    'AWS_LAMBDA_LOG_STREAM_NAME',
    'AWS_LAMBDA_RUNTIME_API',
    'AWS_REGION',
    'AWS_SECRET_ACCESS_KEY',
    'AWS_SESSION_TOKEN',
    'AWS_XRAY_CONTEXT_MISSING',
    'AWS_XRAY_DAEMON_ADDRESS',
    'LAMBDA_RUNTIME_DIR',
    'LAMBDA_TASK_ROOT',
    'LANG',
    'LD_LIBRARY_PATH',
    'PATH',
    'PWD',
    'PYTHONPATH',
    'SHLVL',
    'TZ',
    '_AWS_XRAY_DAEMON_ADDRESS',
    '_AWS_XRAY_DAEMON_PORT',
    '_HANDLER',
    '_X_AMZN_TRACE_ID',
    # These seems to be present when warmstarting, but no need to wipe them I guess?
    'AWS_LAMBDA_FUNCTION_VERSION',
    'AWS_SESSION_TOKEN',
]


def main(lambda_event, _):
    print('Environment variables start')
    for key in list(os.environ):
        if key not in COMMON_ENV:
            os.environ.pop(key)
            print(f'Remove {key} from env')

    for environment_variable in lambda_event:
        key, value = environment_variable['name'], environment_variable['value']
        if key in COMMON_ENV:
            print(f'Cannot set reserved variable {key}')
        else:
            os.environ[key] = value

    feedback_and_export()
