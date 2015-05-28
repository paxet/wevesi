# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.admin import Admin
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine

from . import config
from .blueprints.base import base_listener
from .blueprints.products import products_listener

app = Flask(__name__)
app.config.from_object(config)

# Jinja Prettiness
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Initialize extensions
admin = Admin(app)
crypt = Bcrypt(app)
db = MongoEngine(app)
login_manager = LoginManager(app)

# Initialize blueprints
app.register_blueprint(baselistener)
app.register_blueprint(products_listener, url_prefix='/products')


@app.errorhandler(401)
def forbidden_401(exception):
    return render_template('401.html'), 401


@app.errorhandler(403)
def forbidden_403(exception):
    return render_template('403.html'), 403


@app.errorhandler(404)
def forbidden_404(exception):
    return render_template('404.html'), 404

