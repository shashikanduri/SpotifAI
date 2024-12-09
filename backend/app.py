from main import create_app
from pprint import pprint
from flask import session
import traceback
from main.api_exceptions import APIError


# create flask app
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


# before request tasks
@app.before_request
def before_request_tasks():

    try:

        # check token expiry and refresh if needed
        token_info = session.get('token_info')

        if token_info:
            sp_oauth = app.config['SP_OAUTH']
            if sp_oauth.is_token_expired(token_info):
                token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
                session['token_info'] = token_info

    except Exception as e:
        api_exception_response, status_code = handle_exception(APIError(e, e.__str__(), traceback.format_tb(e.__traceback__)))
        return api_exception_response, status_code
    
    
