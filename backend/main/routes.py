from flask import Blueprint, jsonify, current_app, request, session
from pprint import pprint
from .decorators import require_params
from main import utils
from main.api_exceptions import APIError
import traceback


spotify_api = Blueprint('spotify_api', __name__)

# send client_id and other deets when required for auth page
@spotify_api.route('/get-client', methods=['GET'])
def get_client():

    return jsonify({
        "client_id" : current_app.config['CLIENT_ID'],
        "scope" : current_app.config['SPOTIFY_SCOPES'],
        "spotify_auth_url" : current_app.config['SPOTIFY_AUTH_URL']
    }), 200



# get access token with the code received from spotify auth page
@spotify_api.route("/login", methods = ['POST'])
@require_params("code")
def signin():

    try:
        response = {
            "message": "",
            "data": None,
            "status": 1
        }

        # get access token and user_info from spotify
        token_info, user_info = utils.get_access_token(code = request.json['code'])

        if token_info and user_info:
            session['token_info'] = token_info
            session['user_info'] = { 'user_id' : user_info['id'], 'user_name' : user_info['display_name'] }
            response['message'] = "signed in!"
            response['data'] = { 'user_name' : user_info['display_name'] }
            response = jsonify(response)

        return response, 200

    except Exception as e:
        raise APIError(e, e.__str__(), traceback.format_tb(e.__traceback__))
    


# dashboard
@spotify_api.route("/dashboard", methods = ['GET'])
def dashboard():
    
    try:
        response = {
            "message": "",
            "data": None,
            "status": 1
        }

        # get dashboard info
        dashboard_info = utils.get_dashboard_info(session['token_info']['access_token'])
        response['data'] = dashboard_info
        response = jsonify(response)

        return response, 200

    except Exception as e:
        raise APIError(e, e.__str__(), traceback.format_tb(e.__traceback__))
    

# logout
@spotify_api.route("/logout", methods = ['GET'])
def logout():
    
    try:
        response = {
            "message": "signed out !",
            "data": None,
            "status": 1
        }

        session.clear()

        return response, 200

    except Exception as e:
        raise APIError(e, e.__str__(), traceback.format_tb(e.__traceback__))
    






@spotify_api.route('/health', methods=['GET'])
def health():
    return "OK", 200
