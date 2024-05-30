from flask import Flask
from app.config import get_logger
from app.controller import prediction_app
from .db import db
from flask_session import Session



_logger = get_logger(logger_name=__name__)
#create app

def create_app(*, config_object)->Flask:
    """Create a flask app instance"""
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_object)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    # Configure session to use signed cookies
    flask_app.config['SESSION_TYPE'] = 'filesystem'
    flask_app.config['SESSION_PERMANENT'] = False
    Session(flask_app)

    
    #Initialize database
    db.init_app(flask_app)
    with flask_app.app_context():
        db.create_all()
    
    # Import blueprints
    flask_app.register_blueprint(prediction_app)
    _logger.debug('Application Instance Created')

    return flask_app