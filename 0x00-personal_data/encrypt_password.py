#!/usr/bin/env python3
'''encrypt password using bcrypt'''


import bcrypt


def hash_password(password: str) -> bytes:
    '''defining the function'''
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_password
