#!/usr/bin/env python3

from sys import stderr
from time import time
from os import path, remove, sep, mkdir
from flask import Flask, request, redirect, session
from flask.helpers import make_response
from flask_babel import Babel, gettext
from flask.templating import render_template
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
from analyze import Loglevel, analyze_logfile
from helpers import bytes_to_unit
try:
    from config import ANALYZER_CFG, SERVER_CFG
except ImportError:
    from config_default import ANALYZER_CFG, SERVER_CFG

app = Flask(__name__)
babel = Babel(app)

ALLOWED_EXTS = ANALYZER_CFG.get('allowed_extensions', [])
ALLOWED_FILETYPES = ','.join([f'.{ext}' for ext in ALLOWED_EXTS])
LOGLEVELS = [l.name for l in Loglevel]
DATA_DIR = ANALYZER_CFG.get('data_dir', 'data')

if not path.exists(DATA_DIR):
    for sub_path in DATA_DIR.split(sep):
        if not path.exists(sub_path):
            mkdir(sub_path)

app.config.update({
    'MAX_CONTENT_LENGTH': SERVER_CFG.get('max_upload_size', 20000000),
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
        'SelFileDesc': gettext('Please select a Arma 3 Logfile in one of the following file format: '),
        'SelLoglevel': gettext('Select the minimum loglevel'),
        'SelLoglevelDesc': gettext('The lowest shown Error Level. Lower means more information will be gathered from your log.'),
        'Upload': gettext('Upload'),
        'UploadFile': gettext('Upload Logfile'),
        'UploadAnother': gettext('Upload another logfile'),
        'Output': gettext('Analysis results'),
        'FoundErrors': gettext('Log Errors found:'),
        'ErrInLevel': gettext('Results in log level:'),
        'NoErrors': gettext('No errors have been found, good job!'),
        'MaxSize': gettext('Maximum allowed filesize: '),
        'TooLarge': gettext('The uploaded file exceeded the maximum allowed filesize. Please try again with a different file.'),
        'UnicodeError': gettext('An Unicode Error occured. We are aware of the issue and working on a solution. In the meantime, please copy the contents of your logfile, paste it into an empty txt file and try agian.'),
        'UnknownError': gettext('An unknown error occured. Your file has been saved and the issue will be investigated.')
    }


@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        return request.args.get('lang')

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
        return render_template('index.html', title=gettext('UploadFile'), supported_filetypes=ALLOWED_FILETYPES, levels=LOGLEVELS, max_size=bytes_to_unit(app.config.get('MAX_CONTENT_LENGTH')), error=request.args.get('error'))

    if request.method == 'POST':
        try:
            # check if the post request has the file part
            if 'file' not in request.files:
                return redirect('/')

            file = request.files['file']
            if file.filename == '':
                return redirect('/')

            res = None

            if file and allowed_file(file.filename):
                filename = path.join(DATA_DIR, secure_filename(
                    f'{round(time())}_{file.filename}'))

                file.save(filename)
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        res = analyze_logfile(
                            f, Loglevel[request.form['loglevel']])
                except UnicodeDecodeError:
                    try:
                        with open(filename, 'r', encoding='latin-1') as f:
                            res = analyze_logfile(
                                f, Loglevel[request.form['loglevel']])
                    except UnicodeDecodeError:
                        print(e, file=stderr)
                        return redirect('/?error=UnicodeError')

                remove(filename)

                has_errors = False
                for v in res.values():
                    if v:
                        has_errors = True
                        break

            return render_template('output.html', title=gettext('Output'), results=res, has_err=has_errors)
        except RequestEntityTooLarge as e:
            print(e, file=stderr)
            return redirect('/?error=TooLarge')
        except UnicodeDecodeError as e:
            print(e, file=stderr)
            return redirect('/?error=UnicodeError')
        except Exception as e:
            print(e, file=stderr)
            return redirect('/?error=UnknownError')


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
