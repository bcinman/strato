from wsgiref.util import setup_testing_defaults
from strato import Request

environ = {
    'REQUEST_METHOD': 'PUT',
    'HTTP_HOST': 'example.com',
    'PATH_INFO': '/path',
    'SERVER_PORT': '80'
}

setup_testing_defaults(environ)

request = Request(environ)

def test_host():
    assert request.host == 'example.com'

def test_method():
    assert request.method == 'PUT'

def test_path_info():
    assert request.path_info == '/path'

def test_port():
    assert request.port == 80

def test_query_string():
    assert request.query_string == None
    request.env['QUERY_STRING'] = 'param=value'
    assert request.query_string == 'param=value'

def test_content_type():
    assert request.content_type == None
    request.env['CONTENT_TYPE'] = 'text/plain'
    assert request.content_type == 'text/plain'

def test_content_length():
    assert request.content_length == 0
    request.env['CONTENT_LENGTH'] = '1024'
    assert request.content_length == 1024

def test_params():
    assert request.params == {}