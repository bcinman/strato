from strato import Router, Request
from strato.route import Route
from .support import create_test_environ

def handler(request):
    pass

router = Router()
router.route('/test', handler, methods=['GET'])
router.route('/test2/{id}', handler, methods=['GET'])

def test_route_adds_to_routes():
    assert Route('/test', handler, methods=['GET']).__dict__ == router.routes[0].__dict__

def test_routes_to_handler():    
    environ = create_test_environ(
        path_info='/test2/42', 
        request_method='GET')
    matched_handler, _ = router.match(environ)
    assert matched_handler == handler 


def test_routes_to_404_if_no_matching_route():
    environ = create_test_environ(
        path_info='/test/42', 
        request_method='GET')
    matched_handler, _ = router.match(environ)
    assert matched_handler == Router.not_found

# TODO: Figure out how to test WSGI applications
# def test_wsgi_app():
#     def index():
#         return (200, 'Hello World', ('Content-type', 'text/plain'))
#     router.route('/index', index, methods=['GET'])
#     environ = create_test_environ(path_info='/index')
#     server = make_server('', 8000, router)
#     request = WSGIRequestHAndler(server)

# def test_adds_params_to_environ():
#     environ = create_test_environ(
#         path_info='/test/42', 
#         request_method='GET')
#     router(environ)
#     assert environ['strato.params'] == {'id': '42'}