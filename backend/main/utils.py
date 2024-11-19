import requests
from flask import current_app, Request
import base64
from pprint import pprint

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
    
    if spotify_response.status_code == 200:
        data = spotify_response.json()
        pprint(data)
        return data
    
    return {}
    