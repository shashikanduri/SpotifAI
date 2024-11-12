
class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CLIENT_ID = "a57beb060c7a4a00b0794bfe983fede8"
    CLIENT_SECRET = "df87c58d10e2449c9b77ba02db612f96"
    SPOTIFY_SCOPES = "user-read-currently-playing playlist-read-private playlist-modify-private user-read-email"
    SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"