from os import getenv as env

ANALYZER_CFG = {
    'allowed_extensions': ['txt', 'rpt']
}

SERVER_CFG = {
    'session_secret':       env('SESSION_SECRET', 'supersecret'),
    'session_cookie_name':  env('SESSION_COOKIE', 'armalog_session'),
    'hostname':             env('HOSTNAME', 'localhost'),
    'port':                 int(env('PORT', '8000')),
    'ssl': {
        'certfile': env('CERTFILE', ''),
        'keyfile':  env('KEYFILE', '')
    }
}
