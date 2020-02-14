from flask import Flask, g
from flask_session import Session
from flask_redis import FlaskRedis
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Globally accessible libraries
# db = 
r = FlaskRedis()


def create_app():
    """Initialize the core application."""
    app = FLask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

