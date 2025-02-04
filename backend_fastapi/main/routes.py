
from fastapi import APIRouter
from pprint import pprint
from .dependencies import settings
from urllib.parse import urlencode, urljoin
from fastapi import APIRouter, HTTPException, status

# spotify_api = Blueprint('spotify_api', __name__)

spotify_api = APIRouter()

# send client_id and other deets when required for auth page
@spotify_api.get('/authorize')
def authorize(settings: settings):

    try:

        # Parameters to be included in the query
        params = {
            "client_id" : settings['CLIENT_ID'],
            "response_type" : "code",
            "redirect_uri" : settings['SP_OAUTH'].redirect_uri,
            "state" : "lol",
            "scope" : settings['SPOTIFY_SCOPES'],
            "show_dialog" : True
        }

        auth_url = urljoin(settings['SPOTIFY_AUTH_URL'], '?' + urlencode(params))

        return { "url" : auth_url }
    
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = e.__str__())
