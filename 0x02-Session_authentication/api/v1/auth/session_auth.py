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
