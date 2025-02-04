from flask import current_app
from spotipy import Spotify
from main.api_exceptions import SpotifyError
from pprint import pprint


# get access token on signin
def get_access_token(code : str) -> dict:

    token_info = current_app.config['SP_OAUTH'].get_access_token(code = code, check_cache = False, as_dict = True)

    # USER INFO
    sp = Spotify(auth = token_info['access_token'])
    user_info = sp.current_user()
    
    if token_info and user_info:
        return token_info, user_info
    
    raise SpotifyError(token_info)
    

# get dashboard info
def get_dashboard_info(access_token: str) -> dict:

    response = {
        "playlists" : []
    }

    sp = Spotify(auth = access_token)
    
    # PLAYLISTS
    playlists = sp.current_user_playlists()
    response['playlists'] = playlists
    
    return response