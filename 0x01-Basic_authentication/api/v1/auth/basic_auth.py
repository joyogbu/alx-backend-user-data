#!/usr/bin/env python3
'''basic_auth class that inherits from auth'''

from flask import request
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''Basic Auth that inherits from Auth
    '''
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''function to extract base64 of authorization header
        '''
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not(authorization_header.startswith('Basic ')):
            return None
        arguments = authorization_header.split()
        return (arguments[1])
