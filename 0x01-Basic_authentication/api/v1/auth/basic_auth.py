#!/usr/bin/env python3
'''basic_auth class that inherits from auth'''


import base64
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
from models.base import Base
from typing import TypeVar


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
        others = []
        others.append(decoded_str[1:])
        mypass = ":".join(decoded_str[1:])
        return (decoded_str[0], mypass)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        '''returns the user instance based on email and password'''
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        '''valid = User().is_valid_password(user_pwd)
        if valid is False:
            return None'''
        '''my_obj = User.load_from_file()
        if my_obj is None:
            return None'''
        try:
            my_user = User.search({"email": user_email})
            if not my_user or my_user == []:
                return None
            for user in my_user:
                if user.is_valid_password(user_pwd):
                    # if user_email not in my_user:
                    return user
                    '''else:
                    return (user)'''
        except exception as e:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''retrieves a user instance for a request'''
        a1 = Auth().authorization_header(request)
        a2 = self.extract_base64_authorization_header(a1)
        a3 = self.decode_base64_authorization_header(a2)
        a4 = self.extract_user_credentials(a3)
        a5 = self.user_object_from_credentials(a4[0], a4[1])
        return (a5)
