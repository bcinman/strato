import re
from strato.route import Route

class Router(object):
    def __init__(self):
        self.routes = []

    def __call__(self, environ, start_response):
        """WSGI app callable"""
        handler, params = self.match(environ)
        environ['strato.params'] = params
        return handler(environ, start_response)

    def route(self, pattern, handler, methods=['GET']):
        """Append a Route to this router"""
        route = Route(pattern, handler, methods=methods)
        self.routes.append(route)
    
    def match(self, environ):
        """Matches the provided wsgi `environ` to first matching Route or 
        a generic 404 handler if no route is matched."""
        for route in self.routes:
            result = route.match(environ)
            if result[0]:
                return result
        return Router.not_found, {}

    def not_found(environ, start_response):
        """Generic 404 handler"""
        start_response('404', [('Content-type', 'text/plain')])
        return "404 Not Found"