from flask import Blueprint, jsonify, current_app, request, session, redirect
from pprint import pprint
from main import utils
from main.api_exceptions import APIError
import traceback
from urllib.parse import urlencode, urljoin


spotify_api = Blueprint('spotify_api', __name__)

# send client_id and other deets when required for auth page
@spotify_api.route('/authorize', methods = ['GET'])
def authorize():

    try:

        # Parameters to be included in the query
        params = {
            "client_id" : current_app.config['CLIENT_ID'],
            "response_type" : "code",
            "redirect_uri" : current_app.config['SP_OAUTH'].redirect_uri,
            "state" : "lol",
            "scope" : current_app.config['SPOTIFY_SCOPES'],
            "show_dialog" : True
        }

        auth_url = urljoin(current_app.config['SPOTIFY_AUTH_URL'], '?' + urlencode(params))

        return jsonify({ "url" : auth_url }), 200
    
    except Exception as e:
        raise APIError(e, e.__str__(), traceback.format_tb(e.__traceback__))
    
# callback from spotify, get access token and send to frontend
@spotify_api.route('/callback', methods = ['GET'])
def callback():

    try:
        code = request.args.get('code')

        # get access token and user_info from spotify
        token_info, user_info = utils.get_access_token(code = code)

        if token_info and user_info:
            session['token_info'] = token_info
            session['user_info'] = { 'user_id' : user_info['id'], 'user_name' : user_info['display_name'] }

        fe_callback = urljoin(current_app.config['FE_URL'], '?' + urlencode({ "status" : "ok", "display_name" : user_info['display_name'] }))

        return redirect(fe_callback)

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
