#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import unittest
import uuid
import os

from flask import current_app
from flask.ext.login import LoginManager, login_required, login_user

class BullTestCase(unittest.TestCase):
    def setUp(self):
        pass


    def test_get_test(self):
        pass


    def test_get_user(self):
        pass


    def login(self, username, password):
        """Login user."""
        return self.app.post(
                '/login', 
                data={'email': username, 'password': password},
                follow_redirects=True
                )


    def test_user_authentication(self):
        pass
