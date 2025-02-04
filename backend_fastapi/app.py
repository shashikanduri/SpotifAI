from main import create_app
from pprint import pprint
from flask import session
import traceback
from main.api_exceptions import APIError


# create fastapi app
app = create_app()
    
