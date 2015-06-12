#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_debugtoolbar import DebugToolbarExtension
from wevesi import app


def get_app():
    """Return the application object."""
    return app

if __name__ == '__main__':
    get_app().debug = True
    toolbar = DebugToolbarExtension(get_app())
    get_app().run()

