from wsgiref.util import setup_testing_defaults

def create_test_environ(**kwargs):
    environ = {}
    setup_testing_defaults(environ)
    for k, v in kwargs.items():
        environ[k.upper()] = v
    return environ