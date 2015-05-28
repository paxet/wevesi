from flask import flash
from mongoengine import Document
from mongoengine.fields import StringField, EmailField, BooleanField, IntField

from wevesi import crypt

class User(Document):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    validated = BooleanField(default=False)
    user_type = StringField(default='user')
    active = BooleanField(default=True)
    login_attempts = IntField(default=0)


class UserObj(object):
    def __init__(self, user_obj=None):
        self._user_obj = user_obj


    @staticmethod
    def get(user_id):
        return User.objects(email=user_id).first()


    @staticmethod
    def login(user_id, password):
        valid = False
        user = None
        document = User.objects(email=user_id).first()
        if document:
            valid = crypt.check_password_hash(document['password'], password)
        if valid:
            user = UserObj(document)
            user.authenticated = True
        return user


    @staticmethod
    def create(name, user_id, password):
        user_created = False
        passwd_hash = crypt.generate_password_hash(password)
        try:
            User(name=name, email=user_id, password=passwd_hash).save()
        except Exception as e:
            flash(e.message, 'danger')
            user_created = False
        else:
            user_created = True
        return user_created


    def get_id(self):
        return getattr(self._user_obj, 'email', None)

    def is_authenticated(self):
        return getattr(self, 'authenticated', None)


    def is_active(self):
        return getattr(self._user_obj, 'active', None)


    def is_anonymous(self):
        return False

