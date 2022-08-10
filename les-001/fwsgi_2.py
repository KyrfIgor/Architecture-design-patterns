from wsgiref.simple_server import make_server

def application(environ, start_responce):
    start_responce('200 ok', [('content-type', 'text/html')])
    return[b'Hello world from a simple WSGI application']


with make_server('', 8000, application) as httpd:
    print('server runs on port 8000')
    httpd.serve_forever()