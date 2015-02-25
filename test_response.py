from strato.response import response
def test_status_string():
    status, body, headers = response('Test', status=200)
    assert status == '200 OK'

def test_convert_body_to_bytes():
    status, body, headers = response('Test', status=200)
    assert type(body) == bytes