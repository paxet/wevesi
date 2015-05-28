#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_debugtoolbar import DebugToolbarExtension
from webesi import app


def get_app():
    """Return the application object."""
    return app

if __name__ == '__main__':
    get_app().debug = True
    toolbar = DebugToolbarExtension(app)
    get_app().run()

