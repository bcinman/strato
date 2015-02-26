import re

class Route(object):
    def __init__(self, pattern, handler, methods=None):
        self.methods = methods or ['GET']
        self.pattern = pattern
        self.handler = handler
        self.regex = Route.compile(self.pattern)

    def match(self, environ) -> (callable or False, dict or None):
        """Checks if the given `environ` matches this route"""
        if environ['REQUEST_METHOD'] in self.methods:
            matcher = self.regex.match(environ['PATH_INFO'])
            if matcher:
                return self.handler, matcher.groupdict()
        return False, None
        
    def compile(pattern):
        """Compile the pattern into a regex object"""
        parser = re.compile(r'{(\w+)}')
        def param_regex(match):
            return '(?P<' + match.group(1) + '>[\w-]+)'
        matcher, _ = parser.subn(param_regex, pattern)
        matcher = '^' + matcher + '$'
        return re.compile(matcher)
        