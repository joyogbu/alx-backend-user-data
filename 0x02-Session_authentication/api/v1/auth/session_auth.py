#!/usr/bin/env python3
'''session auth that inherits from Auth class'''


import base64
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class SessionAuth(Auth):
    '''class inherits from Auth'''
    pass
