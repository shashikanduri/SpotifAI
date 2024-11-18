from flask import Blueprint, jsonify, current_app
from pprint import pprint

spotify_api = Blueprint('spotify_api', __name__)

@spotify_api.route('/get-client', methods=['GET'])
def get_client():

    return jsonify({
        "client_id" : current_app.config['CLIENT_ID'],
        "scope" : current_app.config['SPOTIFY_SCOPES'],
        "spotify_auth_url" : current_app.config['SPOTIFY_AUTH_URL']
    }), 200

@spotify_api.route('/playlists')
def getUserPlaylists():
    
    return {}