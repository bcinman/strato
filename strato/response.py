def text(body, status=200):
    return response(body, status, 'text/plain')

def html(body, status=200):
    return response(body, status, 'text/html')

def json(body, status=200):
    return response(body, status, 'application/json')

def response(body, status=200, content_type='text/plain', headers=None):
    if headers is None:
        headers = []
    headers.append(('Content-type', content_type))
    status = str(status)
    return status, body, headers