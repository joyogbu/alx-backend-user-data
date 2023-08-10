#!/usr/bin/env python3
'''basic_auth class that inherits from auth'''

from flask import request
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''Basic Auth that inherits from Auth
    '''
    pass
