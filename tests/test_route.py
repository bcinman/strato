from strato import Request
from strato.route import Route
from .support import create_test_environ

def action(request):
    pass

def test_compile_static_pattern():
    regex = Route.compile("/test")
    assert regex.pattern == r'^/test$'

def test_compile_dynamic_pattern():
    regex = Route.compile("/test/{id}")
    assert regex.pattern == r'^/test/(?P<id>[\w-]+)$'

def test_compile_dynamic_pattern_2():
    regex = Route.compile("/test/{one}/nested/{two}")
    assert regex.pattern == r'^/test/(?P<one>[\w-]+)/nested/(?P<two>[\w-]+)$'

def test_matches_static_path():
    route = Route('/test', action, methods=['GET'])
    environ = create_test_environ(
        request_method='GET',
        path_info='/test')
    handler, params = route.match(environ)
    assert handler
    assert params == {}

def test_matches_dynamic_path():
    route = Route('/test/{id}', action, methods=['GET'])
    environ = create_test_environ(
        request_method='GET',
        path_info='/test/42')
    handler, params = route.match(environ)
    assert handler
    assert params == {'id': '42'}

def test_methods_defaults_to_get():
    route = Route('/test/{id}', action)
    assert route.methods == ['GET']