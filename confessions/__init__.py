import os

from flask import Flask, g
from flask_session import Session
from flask_redis import FlaskRedis
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Globally accessible libraries
# db = 
r = FlaskRedis()


def create_app(test_config=None):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'confessions.sqlite')
    )

