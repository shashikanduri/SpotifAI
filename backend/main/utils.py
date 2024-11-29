import requests
from flask import current_app, Request
import base64
from spotipy import Spotify, SpotifyOAuth
from main.api_exceptions import SpotifyError
from pprint import pprint
from config import Config


# get access token on signin
def get_access_token(code : str) -> dict:

    token_info = current_app.config['SP_OAUTH'].get_access_token(code = code, as_dict = True)

    # USER INFO
    sp = Spotify(auth = token_info['access_token'])
    user_info = sp.me()
    token_info['user_id'] = user_info['id']
    token_info['user_name'] = user_info['display_name']
    
    if token_info:
        return token_info
    
    raise SpotifyError(token_info)
    

# get dashboard info
def get_dashboard_info(token_info: dict) -> dict:

    response = {
        "playlists" : []
    }

    sp = Spotify(auth = token_info['access_token'])
    
    # PLAYLISTS
    playlists = sp.user_playlists(token_info['user_id'])
    response['playlists'] = playlists
    
    return response