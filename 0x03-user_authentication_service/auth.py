#!/usr/bin/env python3
'''takes a password string argument and returns a bytes'''


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    '''take a string password and return a byte'''
    pass_str = password.encode('utf-8')
    salt = bcrypt.gensalt()
    pass_hash = bcrypt.hashpw(pass_str, salt)
    return pass_hash


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        '''initializing the class'''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''take in attributes and return a User object'''
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                raise ValueError("User {} already exists".format(user.email))
        except NoResultFound as err:
            passwd = _hash_password(password)
            new_user = self._db.add_user(email, passwd)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        '''validate login for users'''
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                pass_str = password.encode('utf-8')
                if not bcrypt.checkpw(pass_str, user.hashed_password):
                    return False
                else:
                    return True
        except NoResultFound as err:
            return False

def _generate_uuid():
    '''generate a return a string representation of a new uuid'''
    new_uuid = uuid.uuid4()
    return str(new_uuid)
