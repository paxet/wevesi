#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_admin import Admin
from flask_admin.contrib.mongoengine import ModelView

from wevesi.models.user import User


class UserView(ModelView):
    pass

admin = Admin()
admin.add_view(UserView(User))
