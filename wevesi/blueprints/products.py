from flask import Blueprint, render_template

products_listener = Blueprint('products', __name__)


@products_listener.route('/')
def list_products():
    return ''

