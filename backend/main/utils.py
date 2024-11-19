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
    

# get user info
def get_user_info(access_token):

    request_headers = {
        "Authorization" : f"Bearer {access_token}"
    }

    spotify_response = requests.get(url = "https://api.spotify.com/v1/me", headers = request_headers)
    spotify_response_data = spotify_response.json()

    pprint(spotify_response_data)

    if spotify_response.status_code == 200:
        return spotify_response_data
    
    raise SpotifyError(spotify_response_data)
    