from flask import Flask, url_for
from flask_cors import CORS
from .routes import spotify_api
from config import Config
from spotipy import SpotifyOAuth


# app factory pattern - create flask app and set configs
def create_app():
    
    app = Flask(__name__)
    CORS(app, methods = ["GET", "POST", "OPTIONS"], supports_credentials = True)

    # register blueprints
    app.register_blueprint(spotify_api)

    # set configs
    app.config.from_object(Config())
    
    # set spotify oauth
    with app.app_context():    
        app.config['SP_OAUTH'] = SpotifyOAuth(
                            client_id = app.config['CLIENT_ID'],
                            client_secret = app.config['CLIENT_SECRET'],
                            redirect_uri = url_for('spotify_api.callback', _external = True),
                            scope = app.config['SPOTIFY_SCOPES']
                        )

    return app
