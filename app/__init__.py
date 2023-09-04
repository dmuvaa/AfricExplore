from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """function to create a Flask app instane
    Then set the secret key for the Flask app used for session handling
    Set the database URI for SQLAlchemy.
    Here it's set to use a SQLite database named "site.db
    """
    app = Flask(__name__)
    app.config.from_pyfile('../config.py') 

    """Initialize and bind the database instance (db)
    to this Flask application instance
    """
    #db.init_app(app)

    """
    Importing the "auth" blueprint from the routes module
    and registering it with the Flask application
    Importing the "destinations" blueprint
    from the routes module and registering it with the Flask application.
    This is used to modularize and organize
    the codebase for destination related routes
    """
    #from .routes import auth as auth_blueprint
    #app.register_blueprint(auth_blueprint)

    from .routes import destinations
    app.register_blueprint(destinations.bp)

    """return the flask application instance"""
    return app
