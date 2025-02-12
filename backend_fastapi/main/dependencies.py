from config import Settings
from functools import lru_cache
from typing import Annotated
from fastapi import Depends
from spotipy import SpotifyOAuth


@lru_cache
def get_settings(redirect_uri: str):
    return Settings(redirect_uri)
settings = Annotated[Settings, Depends(get_settings)]