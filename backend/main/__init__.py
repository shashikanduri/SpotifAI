from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .routes import spotify_api
from config import Config
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    CORS(app, methods = ["GET", "POST", "OPTIONS"], supports_credentials = True)
    app.config.from_object(Config())

    db.init_app(app)

    app.register_blueprint(spotify_api)

    with app.app_context():
        db.create_all()
    
    jwt_app = JWTManager(app)

    return app
