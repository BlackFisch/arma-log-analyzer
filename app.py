#!/usr/bin/env python3

from flask import Flask
from time import time
from os import path, remove
from flask import request, redirect
from flask.templating import render_template
from werkzeug.utils import secure_filename
from analyze import Loglevel, analyze_logfile
from config import ANALYZER_CFG

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

ALLOWED_EXTS = ANALYZER_CFG.get('allowed_extensions', [])
ALLOWED_FILETYPES = ','.join([f'.{ext}' for ext in ALLOWED_EXTS])
LOGLEVELS = [l.name for l in Loglevel]
LOGLEVELS.reverse()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTS


@app.route('/', methods=['POST', 'GET'])
def landing():
    if request.method == 'GET':
        return render_template('index.html', supported_filetypes=ALLOWED_FILETYPES, levels=LOGLEVELS)

    # check if the post request has the file part
    if 'file' not in request.files:
        return redirect(request.url)

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

    return render_template('index.html', results=res, has_err=has_errors)
