import os

from flask import Flask, g, session
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='placeholder'#PATH TO DATABASE
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('config.Config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Include routes
        from . import routes

        # Create tables
        db.create_all()

        return app




