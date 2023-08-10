#!/usr/bin/env python3
'''basic_auth class that inherits from auth'''


import base64
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

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        '''decode the authorization header'''
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            res = base64_authorization_header.encode('utf-8')
            res_str = base64.b64decode(res)
            result = res_str.decode('utf-8')
            return (result)
        except ValueError:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        '''returns the decoded value '''
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if not(':' in decoded_base64_authorization_header):
            return None, None
        decoded_str = decoded_base64_authorization_header.split(':')
        return (decoded_str[0], decoded_str[1])
