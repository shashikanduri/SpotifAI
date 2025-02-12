from pydantic_settings import BaseSettings
from spotipy import SpotifyOAuth

class Settings(BaseSettings):

    client_id = "a57beb060c7a4a00b0794bfe983fede8"
    client_secret = "df87c58d10e2449c9b77ba02db612f96"
    spotify_scopes = "user-read-currently-playing playlist-read-private playlist-modify-private user-read-email user-top-read"
    spotify_oauth_url = "https://accounts.spotify.com/authorize"
    redirect_uri: str

    spotify_oauth = SpotifyOAuth(
                        client_id = client_id,
                        client_secret = client_secret,
                        redirect_uri = redirect_uri,
                        scope = spotify_scopes
                    )