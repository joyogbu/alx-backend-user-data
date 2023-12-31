#!/usr/bin/env python3
'''session auth that inherits from Auth class'''


import base64
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import uuid


class SessionAuth(Auth):
    '''class inherits from Auth'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''creates a session id for a user id'''
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        sessid = str(uuid.uuid4())
        self.user_id_by_session_id[sessid] = user_id
        return (sessid)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''return a user id based on a session id'''
        if session_id is None:
            return None
        if type(session_id) != str:
            return None
        val = self.user_id_by_session_id.get(session_id)
        return val

    def current_user(self, request=None):
        '''return a user instance based on a cookie value'''
        cookie_value = self.session_cookie(request)
        if cookie_value is None:
            return None
        userid = self.user_id_for_session_id(cookie_value)
        '''if userid is None:
            return None'''
        user = User.get(userid)
        return user

    def destroy_session(self, request=None):
        '''deletes the session/logout'''
        if request is None:
            return False
        cookie_val = self.session_cookie(request)
        if not cookie_val or cookie_value is None:
            return False
        userid = self.user_id_for_session(cookie_val)
        if not userid or userid is None:
            return False
        self.user_id_for_session.pop(cookie_val)
        return True
