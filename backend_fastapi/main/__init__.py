from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .routes import spotify_api

# app factory pattern - create flask app and set configs
def create_app():
    
    # create app
    app = FastAPI()

    # cors
    app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"],
    )

    # routes
    app.include_router(spotify_api)

    return app
