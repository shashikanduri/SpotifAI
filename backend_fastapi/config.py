from pydantic_settings import BaseSettings
from spotipy import SpotifyOAuth
from app import app

class Settings(BaseSettings):

    client_id = "a57beb060c7a4a00b0794bfe983fede8"
    client_secret = "df87c58d10e2449c9b77ba02db612f96"
    spotify_scopes = "user-read-currently-playing playlist-read-private playlist-modify-private user-read-email user-top-read"
    spotify_oauth_url = "https://accounts.spotify.com/authorize"

    spotify_oauth = SpotifyOAuth(
                        client_id = client_id,
                        client_secret = client_secret,
                        redirect_uri = app.url_path_for('spotify_api.callback', _external = True),
                        scope = spotify_scopes
                    )