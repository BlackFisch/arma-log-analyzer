#!/usr/bin/env python3

from time import time
from os import path, remove
from flask import Flask, request, redirect, session
from flask.helpers import make_response
from flask_babel import Babel, gettext
from flask.templating import render_template
from werkzeug.utils import secure_filename
from analyze import Loglevel, analyze_logfile
try:
    from config import ANALYZER_CFG, SERVER_CFG
except ImportError:
    from config_default import ANALYZER_CFG, SERVER_CFG

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
babel = Babel(app)

ALLOWED_EXTS = ANALYZER_CFG.get('allowed_extensions', [])
ALLOWED_FILETYPES = ','.join([f'.{ext}' for ext in ALLOWED_EXTS])
LOGLEVELS = [l.name for l in Loglevel]

app.config.update({
    'SECRET_KEY': str(SERVER_CFG.get('secret_key')),
    'SESSION_PERMANENT': False,
    'LANGUAGES': {
        'en': 'English',
        'de': 'Deutsch'
    }
})


@app.context_processor
def inject_conf_var():
    return {
        'cookies_accepted': request.cookies.get('bfme_cookies_accepted'),
        'pageName': 'Arma Log Analyzer',
        'requestedUrl': request.url,
        'AVAILABLE_LANGUAGES': app.config['LANGUAGES'],
        'CURRENT_LANGUAGE': session.get('language', request.accept_languages.best_match(app.config['LANGUAGES'].keys())),
        'LOCALIZED_STRINGS': prepare_texts()
    }


def prepare_texts():
    return {
        'SelFile': gettext('Select file'),
        'SelFileDesc': gettext('Please select a Arma 3 Logfile in rpt or txt file format.'),
        'SelLoglevel': gettext('Select the minimum loglevel'),
        'SelLoglevelDesc': gettext('The lowest shown Error Level. Lower means more information will be gathered from your log.'),
        'Upload': gettext('Upload'),
        'UploadFile': gettext('Upload Logfile'),
        'UploadAnother': gettext('Upload another logfile'),
        'Output': gettext('Analysis results'),
        'FoundErrors': gettext('Log Errors found:'),
        'ErrInLevel': gettext('Results in log level:'),
        'NoErrors': gettext('No errors have been found, good job!')
    }


@babel.localeselector
def get_locale():
    if request.args.lang:
        return request.args.lang
    return request.cookies.get('bfme_pref_lang', request.accept_languages.best_match(app.config['LANGUAGES'].keys()))


@app.route('/accept-cookies')
def accept_cookies():
    res = make_response(redirect(request.args.get('redirect_to', '/')))
    res.set_cookie('bfme_cookies_accepted', 'true',
                   max_age=31536000, domain='.blackfisch.me')
    return res


@app.route('/language=<language>')
def set_language(language=None):
    if not request.cookies.get('bfme_pref_lang'):
        return redirect(f'/?lang={language}')

    res = make_response(redirect('/'))
    res.set_cookie('bfme_pref_lang', 'language',
                   max_age=31536000, domain='.blackfisch.me')
    return res


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTS


@ app.route('/', methods=['POST', 'GET'])
def landing():
    if request.method == 'GET':
        return render_template('index.html', title=gettext('UploadFile'), supported_filetypes=ALLOWED_FILETYPES, levels=LOGLEVELS)

    # check if the post request has the file part
    if 'file' not in request.files:
        return redirect('/')

    file = request.files['file']
    if file.filename == '':
        return redirect('/')

    res = None

    if file and allowed_file(file.filename):
        filename = path.join('data', secure_filename(
            f'{round(time())}_{file.filename}'))

        file.save(filename)
        with open(filename, 'r', encoding='utf-8') as f:
            res = analyze_logfile(f, Loglevel[request.form['loglevel']])

        remove(filename)

        has_errors = False
        for v in res.values():
            if v:
                has_errors = True
                break

    return render_template('output.html', title=gettext('Output'), results=res, has_err=has_errors)
