#!/usr/bin/env python3

from gevent.pywsgi import WSGIServer
from config import SERVER_CFG
from app import app

hostName = SERVER_CFG['hostname']
serverPort = SERVER_CFG['port']
# only use SSL if its defined in config
SSL_CFG = SERVER_CFG['ssl']
secured = len(SSL_CFG) > 0

try:
    http_server = WSGIServer((hostName, serverPort), app, **SSL_CFG)
    print(
        f'Server created at http{"s" if secured else ""}://{hostName}:{serverPort}')
    http_server.serve_forever()
except KeyboardInterrupt:
    pass

print('Webserver stopped.')
