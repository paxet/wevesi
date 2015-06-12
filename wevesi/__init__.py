# -*- coding: utf-8 -*-

from flask import Flask, render_template

from wevesi.crypt import crypt
from wevesi.db import db
from wevesi.blueprints.admin import admin
from wevesi.blueprints.base import base_listener, login_manager
from wevesi.blueprints.products import products_listener

app = Flask(__name__)
app.config.from_object('config')

# Jinja Prettiness
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Initialize extensions
admin.init_app(app)
crypt.init_app(app)
db.init_app(app)
login_manager.init_app(app)

# Initialize blueprints
app.register_blueprint(base_listener)
app.register_blueprint(products_listener, url_prefix='/products')


@app.add_template_filter
def category_or(string, default):
    category = default
    if string in ['success', 'info', 'warning', 'danger']:
        category = string
    return category


@app.errorhandler(401)
def forbidden_401(exception):
    return render_template('401.html'), 401


@app.errorhandler(403)
def forbidden_403(exception):
    return render_template('403.html'), 403


@app.errorhandler(404)
def forbidden_404(exception):
    return render_template('404.html'), 404

