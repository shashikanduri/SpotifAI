from datetime import timedelta

class Config:

    SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CLIENT_ID = "a57beb060c7a4a00b0794bfe983fede8"
    CLIENT_SECRET = "df87c58d10e2449c9b77ba02db612f96"
    SPOTIFY_SCOPES = "user-read-currently-playing playlist-read-private playlist-modify-private user-read-email user-top-read"
    SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
    USE_JWT = True
    PFAS_PROTECTED_ENDPOINTS = ['spotify_api.dashboard']
    JWT_SECRET_KEY = "aNand_SarFrazaHmadMasurkar"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days = 1)
    JWT_COOKIE_SECURE = False
    JWT_TOKEN_LOCATION = ["cookies"]
    # JWT_COOKIE_SAMESITE = 'None'
    JWT_ACCESS_COOKIE_NAME = "sp_access_token"
    JWT_ACCESS_CSRF_COOKIE_NAME = "sp_csrf"