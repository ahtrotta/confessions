from os import environ

class Config(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite:///data.db'
