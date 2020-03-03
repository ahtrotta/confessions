from os import environ

class Config(object):
    
    # general config
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SECRET_KEY = 'temporary-key'
    
    # Flask-Session config
    SESSION_TYPE = 
