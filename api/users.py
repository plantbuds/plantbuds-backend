from server.settings import GOOGLE_CLIENT_ID
from google.oauth2 import id_token
from google.auth.transport import requests


def validate_google_token(token):
    try:
        id_info = id_token.verify_oauth2_token(token, requests.Request())
        userid = id_info['sub']
        print(f'user id: {userid}')
    except ValueError:
        return None
    return id_info
