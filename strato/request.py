class Request(object):
    def __init__(self, environ):
        self.environ = environ

    @property
    def port(self):
        return int(self.environ['SERVER_PORT'])

    @property
    def method(self):
        return self.environ['REQUEST_METHOD']
    
    @property
    def path_info(self):
        return self.environ['PATH_INFO']
    
    @property
    def host(self):
        return self.environ['HTTP_HOST']

    @property
    def query_string(self):
        return self.environ.get('QUERY_STRING', None)

    @property
    def content_type(self):
        return self.environ.get('CONTENT_TYPE', None)

    @property
    def content_length(self):
        return int(self.environ.get('CONTENT_LENGTH', 0))

    @property
    def params(self):
        return self.environ.get('strato.params', {})