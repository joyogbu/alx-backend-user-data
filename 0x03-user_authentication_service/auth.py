#!/usr/bin/env python3
'''takes a password string argument and returns a bytes'''


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import TypeVar, Union


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

    def create_session(self, email: str) -> str:
        '''take an email string and and return a session id'''
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                new_id = _generate_uuid()
                user.session_id = new_id
                return new_id
        except NoResultFound as err:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        '''find user by session id'''
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user is not None:
                return user
            else:
                return None
        except NoResultFound as err:
            return None

    def destroy_session(self, user_id: int) -> None:
        '''find user and destroy the user session'''
        # user = self._db.find_user_by(id=user_id)
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound as err:
            return None


def _generate_uuid() -> str:
    '''generate a return a string representation of a new uuid'''
    new_uuid = uuid.uuid4()
    return str(new_uuid)
