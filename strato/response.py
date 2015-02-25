def text(body, status=200):
    return status, body, [('Content-type', 'text/plain')]

def html(body, status=200):
    return status, body, [('Content-type', 'text/html')]

def json(body, status=200):
    return status, body, [('Content-type', 'application/json')]