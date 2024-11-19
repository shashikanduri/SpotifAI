from flask import Blueprint, jsonify, current_app, request
from pprint import pprint
from .decorators import require_params
from main import utils
from main.api_exceptions import APIError
import traceback
from flask_jwt_extended import create_access_token, set_access_cookies

spotify_api = Blueprint('spotify_api', __name__)

# send client_id and other deets when required
@spotify_api.route('/get-client', methods=['GET'])
def get_client():

    return jsonify({
        "client_id" : current_app.config['CLIENT_ID'],
        "scope" : current_app.config['SPOTIFY_SCOPES'],
        "spotify_auth_url" : current_app.config['SPOTIFY_AUTH_URL']
    }), 200


# receive authorization code from spotify login
@spotify_api.route("/signin", methods = ["POST"])
@require_params("code")
def dashboard():

    try:
        response = {
            "message": "",
            "data": None,
            "status": 1
        }

        # get access token from spotify
        auth_data = utils.get_access_token(request)

        if auth_data:
            response = jsonify(response)

        # set JWT cookies with the access token for frontend
        if current_app.config["USE_JWT"]:
            access_token = create_access_token(identity = auth_data['access_token'], additional_claims = auth_data)
            set_access_cookies(response, access_token)

        return response, 200

    except Exception as e:
        raise APIError(e, e.__str__(), traceback.format_tb(e.__traceback__))