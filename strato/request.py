class Request(object):
    def __init__(self, env):
        self.env = env
        self.params = {}

    @property
    def port(self):
        return int(self.env['SERVER_PORT'])

    @property
    def method(self):
        return self.env['REQUEST_METHOD']
    
    @property
    def path_info(self):
        return self.env['PATH_INFO']
    
    @property
    def host(self):
        return self.env['HTTP_HOST']

    @property
    def query_string(self):
        return self.env.get('QUERY_STRING', None)

    @property
    def content_type(self):
        return self.env.get('CONTENT_TYPE', None)

    @property
    def content_length(self):
        return int(self.env.get('CONTENT_LENGTH', 0))