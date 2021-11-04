from app import app
from gevent.pywsgi import WSGIServer

print('Hello Docker')
print(app)

if __name__ == '__main__':
    http_server = WSGIServer(('localhost', 8000), app)
    print('Started Webserver')
    http_server.serve_forever()
    # http_server.start()
