print(1)
from gevent.pywsgi import WSGIServer
print(2)
from gevent import monkey
print(3)
from app import app
print(4)
try:
    print(5)
    from config import SERVER_CFG
    print(5.1)
except ImportError:
    print(5.2)
    from config_default import SERVER_CFG
    print(5.3)

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
