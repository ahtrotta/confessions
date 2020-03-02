from os import environ

class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SECRET_KEY = 'temporary-key'
