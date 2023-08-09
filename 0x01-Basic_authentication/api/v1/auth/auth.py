#!/usr/bin/env python3
'''auth class to manage authentication'''


from flask import request
from typing import List, TypeVar

class Auth():
    '''class definition to manage authentication
    Methods
    -------
    require_auth: authentication requirement function
    authoruzation_header: manage authorization header
    current_user: authenticate current user
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''authentication function requirement'''
        return False

    def authorization_header(self, request=None) -> str:
        '''define authorization header function'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''define current user function'''
        return None
