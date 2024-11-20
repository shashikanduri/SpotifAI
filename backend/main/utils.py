import requests
from flask import current_app, Request
import base64
from main.api_exceptions import SpotifyError
from pprint import pprint

# get access token on signin
def get_access_token(request : Request) -> dict:

    code = request.json['code']

    # build request data and headers
    access_token_request = {
        "grant_type" : "authorization_code",
        "code" : code,
        "redirect_uri" : "http://localhost:5173"
    }

    client_creds = current_app.config['CLIENT_ID'] + ":" + current_app.config['CLIENT_SECRET']
    auth_header = f"Basic {base64.b64encode(client_creds.encode('utf-8')).decode('utf-8')}"

    request_headers = {
        "Authorization" : auth_header,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    # get access token
    spotify_response = requests.post(url = "https://accounts.spotify.com/api/token", data = access_token_request, headers = request_headers)
    spotify_response_data = spotify_response.json()
    
    if spotify_response.status_code == 200:
        return spotify_response_data
    
    raise SpotifyError(spotify_response_data)
    

# get dashboard info
def get_dashboard_info(access_token):

    response = {
        "user_info" : {},
        "playlists" : [],
        "top_artists" : [],
        "top_tracks" : []
    }

    request_headers = {
        "Authorization" : f"Bearer {access_token}"
    }

    # USER INFO
    spotify_response = requests.get(url = "https://api.spotify.com/v1/me", headers = request_headers)
    spotify_response_data = spotify_response.json()
    
    if spotify_response.status_code == 200:
        response['user_info'] = spotify_response_data
    else:
        raise SpotifyError(spotify_response_data)
    
    # PLAYLISTS
    spotify_response = requests.get(url = f"https://api.spotify.com/v1/users/{response['user_info']['id']}/playlists", headers = request_headers)
    spotify_response_data = spotify_response.json()

    if spotify_response.status_code == 200:
        response['playlists'] = spotify_response_data
    else:
        raise SpotifyError(spotify_response_data)
    
    # USER'S TOP TRACKS
    spotify_response = requests.get(url = f"https://api.spotify.com/v1/me/top/tracks", headers = request_headers)
    spotify_response_data = spotify_response.json()

    if spotify_response.status_code == 200:
        response['top_tracks'] = spotify_response_data
    else:
        raise SpotifyError(spotify_response_data)
    
    # USER'S TOP ARTISTS
    spotify_response = requests.get(url = f"https://api.spotify.com/v1/me/top/artists", headers = request_headers)
    spotify_response_data = spotify_response.json()

    if spotify_response.status_code == 200:
        response['top_artists'] = spotify_response_data
    else:
        raise SpotifyError(spotify_response_data)
    
    return response