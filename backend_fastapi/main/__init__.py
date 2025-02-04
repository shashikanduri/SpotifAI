from .routes import spotify_api
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

# app factory pattern - create flask app and set configs
def create_app():
    
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"],
    )
