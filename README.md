# Strato

Strato is an experimental python web framework. Created solely for the purpose of learning and experimenting with web framework design. **This is not meant to be used in production.**

## Installation
    $ pip install -e 'git+git://github.com/bcinman/strato.git#egg=Package'   

## Usage
```python
from strato import Router
from strato.response import text

router = Router()

def index(request):
    return text('Hello World!')

def name(request):
    return text('Hello {}'.format(request.params['name']))

def new(request)
    return text('This is a post request')

router.get('/', index)
router.get('/{name}', show)

if __name__ == '__main__':
    router.run(4000)
```
You can route on other methods using `post()`, `put()`, `patch()`, `delete()`, and `head()`.

## Handlers
A handler is any callable that takes a request argument and returns a 3-element tuple in the form of __(status, body, headers)__. The strato.response module contains helper methods to quickly create these responses:
```python
from strato.response import text, json, html

def handler_text(request):
    return text('Hello World')

def handler_json(request):
    return json('{"hello": "world"}')

def handler_json(request):
    return html('<b>Hello World</b>')
```

These methods also accept a status code as an argument
```python    
def handler_404(request):
    return text('Not Found', status=404)
```
## TODO
* Proper documentation.
* `form` property on the Request object.
* Provide an actual `Application()` object to handle configuration and middleware.

## Possible Improvements
* Right now matching is only done on the method and path of the request. This could be expanded to match based on any request parameter such as hostname, subdomain, etc...
* Allow for scoping routes. i.e:

```python
  with route.scope('/api') as api:
      api.get('/users', get_users) # matches GET /api/users
```