from os import getenv as env

ANALYZER_CFG = {
    'allowed_extensions':   env('ALLOWED_EXTS', 'txt rpt').split(' '),
    'data_dir':             env('DATA_DIR', 'data')
}

SERVER_CFG = {
    'session_secret':       env('SESSION_SECRET', 'supersecret'),
    'cookie_prefix':        env('COOKIE_PREFIX', 'armalog'),
    'hostname':             env('HOSTNAME', 'localhost'),
    'port':                 int(env('PORT', '8000')),
    'max_upload_size':      int(env('MAX_UPLOAD_SIZE', '50000000')),
    'ssl': {
        'certfile': env('CERTFILE', ''),
        'keyfile':  env('KEYFILE', '')
    }
}
