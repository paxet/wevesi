# from flask import g
# from werkzeug.local import LocalProxy
from flask_mongoengine import MongoEngine

db = MongoEngine()
# dbconn = MongoEngine()


# def get_db():
#     """Opens a new database connection if there is none
#     yet for the current application context."""
#     if not hasattr(g, 'mongo_db'):
#         g.mongo_db = dbconn.connect()
#     return g.mongo_db
#
# db = LocalProxy(get_db)

