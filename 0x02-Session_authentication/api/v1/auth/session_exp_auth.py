#!/usr/bin/env python3
'''session auth that inherits from Auth class'''


import base64
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import uuid
import os


class SessionExpAuth(SessionAuth):
    '''class session exp that inherits from session auth'''
    def __init__(self):
        '''initializing the class'''
        self.os.getenv('SESSION_DURATION')
