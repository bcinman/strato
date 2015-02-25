import re
from wsgiref.simple_server import make_server
from strato import Request
from strato.route import Route
from strato.response import text

class Router(object):
    def __init__(self):
        self.routes = []

    def __call__(self, environ, start_response):
        """WSGI app callable"""
        handler, params = self.match(environ)
        environ['strato.params'] = params
        request = Request(environ)
        status, body, headers = handler(request)
        start_response(status, headers)
        return [body]

    def route(self, pattern, handler, methods=['GET']):
        """Append a Route to this router"""
        route = Route(pattern, handler, methods=methods)
        self.routes.append(route)
    
    def get(self, pattern, handler):
        self.route(pattern, handler, methods=['GET'])

    def post(self, pattern, handler):
        self.route(pattern, handler, methods=['POST'])

    def put(self, pattern, handler):
        self.route(pattern, handler, methods=['PUT'])

    def patch(self, pattern, handler):
        self.route(pattern, handler, methods=['patch'])

    def delete(self, pattern, handler):
        self.route(pattern, handler, methods=['DELETE'])

    def head(self, pattern, handler):
        self.route(pattern, handler, methods=['HEAD'])

    def match(self, environ):
        """Matches the provided wsgi `environ` to first matching Route or 
        a generic 404 handler if no route is matched."""
        for route in self.routes:
            result = route.match(environ)
            if result[0]:
                return result
        return Router.not_found, {}

    def not_found(request):
        """Generic 404 handler"""
        return text("404 Not Found", status=404)

    def run(self, port=4000):
        server = make_server('', port, self)
        server.serve_forever()