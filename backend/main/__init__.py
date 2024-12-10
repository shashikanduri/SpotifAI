from flask import Flask
from flask_cors import CORS
from .routes import spotify_api
from config import Config


def create_app():
    
    app = Flask(__name__)
    CORS(app, methods = ["GET", "POST", "OPTIONS"], supports_credentials = True)
    app.config.from_object(Config())

    app.register_blueprint(spotify_api)

    return app
