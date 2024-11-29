from main import create_app
from pprint import pprint
from flask import request
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, create_access_token, set_access_cookies
import traceback
from datetime import datetime
from main.api_exceptions import APIError

app = create_app()

# ERROR HANDLER
@app.errorhandler(APIError)
def handle_exception(err):

    response = {
                    "error_type": err.type, 
                    "error_details": err.error_details,
                    "traceback": err.traceback,
                    "message": err.message,
                    "status": 0
                }

    return response, err.status_code


# VALIDATE AND PROCESS EVERY INCOMING REQUEST
@app.before_request
def before_request_tasks():

    try:

        if app.config['USE_JWT'] and request.endpoint in app.config['PROTECTED_ENDPOINTS']:
            # verify JWT
            jwt = verify_jwt_in_request()

            # in case of options request, the server listens but does not process anything and the jwt wont exist
            if jwt:
                jwt_header, jwt_data = jwt
                jwt_data['refreshed'] = False
                
                # check access token expiry
                sp_oauth = app.config['SP_OAUTH']
                if sp_oauth.is_token_expired(jwt_data):
                    new_token_info = sp_oauth.refresh_access_token(jwt_data['refresh_token'])
                    new_token_info['user_id'] = jwt_data['user_id']
                    new_token_info['user_name'] = jwt_data['user_name']
                    jwt_data = new_token_info
                    jwt_data['refreshed'] = True

                request.jwt_data = jwt_data


    except Exception as e:
        api_exception_response, status_code = handle_exception(APIError(e, e.__str__(), traceback.format_tb(e.__traceback__)))
        return api_exception_response, status_code
    
    

# PROCESSING AFTER REQUEST IS FINISHED
@app.after_request
def after_request_tasks(response):

    # refresh expiring jwts/access_tokens
    if app.config['USE_JWT']:
        jwt_data = getattr(request, "jwt_data", None)

        if jwt_data:

            # if access token is refreshed, set new cookies
            if jwt_data['refreshed']:
                jwt_data['refreshed'] = False
                access_token = create_access_token(identity = jwt_data['access_token'], additional_claims = jwt_data)
                set_access_cookies(response, access_token)

            # check jwt expiry
            exp_timestamp = jwt_data['exp']
            now = datetime.now()
            target_timestamp = int(datetime.timestamp(now))
            if target_timestamp > exp_timestamp:
                # if both jwt and access_token expire
                if not jwt_data['refreshed']:
                    access_token = create_access_token(identity = get_jwt_identity())

                set_access_cookies(response, access_token)

    return response
    