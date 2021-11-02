#!/usr/bin/env python3

from flask import Flask
from blueprints.main import main_handlers

app = Flask(__name__)
app.register_blueprint(main_handlers)
