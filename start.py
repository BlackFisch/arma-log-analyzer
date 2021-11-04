from app import app
from gevent.pywsgi import WSGIServer

print('Hello Docker')
print(app)

http_server = WSGIServer(('localhost', 8000), app)
print('Started Webserver')
# http_server.serve_forever()
