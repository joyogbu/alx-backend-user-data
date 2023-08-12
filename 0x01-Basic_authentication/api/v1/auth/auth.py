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
        if excluded_paths is None or excluded_paths == []:
            return True
        if path is None:
            return True
        if path[-1] == '/':
            path = path
        else:
            path = path + '/'
        for item in excluded_paths:
            if item[-1] == "*":
                if item[:-1] in path:
                    return False
                    # path = item[:-1]
        if path not in excluded_paths:
            return True
        '''else:'''
        return False

    def authorization_header(self, request=None) -> str:
        '''define authorization header function'''
        if request is None:
            return None
        elif request.headers.get('Authorization') is None:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        '''define current user function'''
        return None
