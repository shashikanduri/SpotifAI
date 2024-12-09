from spotipy import SpotifyOAuth

class Config:

    SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CLIENT_ID = "a57beb060c7a4a00b0794bfe983fede8"
    CLIENT_SECRET = "df87c58d10e2449c9b77ba02db612f96"
    SPOTIFY_SCOPES = "user-read-currently-playing playlist-read-private playlist-modify-private user-read-email user-top-read"
    SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
    SP_OAUTH = SpotifyOAuth(
                            client_id = CLIENT_ID,
                            client_secret = CLIENT_SECRET,
                            redirect_uri = "http://localhost:5173/callback",
                            scope = SPOTIFY_SCOPES
                        )
    SECRET_KEY = 'b7ee0e2de1b5bdede5e21bee6cce30a0ab1079a37cf3df004ebb35e7e1ea12b3'
    SESSION_COOKIE_NAME = 'app_session'
    SESSION_COOKIE_SECURE = False