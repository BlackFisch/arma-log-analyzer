#!/usr/bin/env python3

from gevent.pywsgi import WSGIServer
from gevent import monkey
from app import app
try:
    from config import SERVER_CFG
except ImportError:
    from config_default import SERVER_CFG

print('Setting up PYWSGI server')

monkey.patch_all()

hostName = SERVER_CFG['hostname']
serverPort = SERVER_CFG['port']
# only use SSL if its defined in config
SSL_CFG = SERVER_CFG['ssl']
secured = len(SSL_CFG) > 0

http_server = WSGIServer((hostName, serverPort), app, **SSL_CFG)
print(
    f'Server created at http{"s" if secured else ""}://{hostName}:{serverPort}')
http_server.serve_forever()
