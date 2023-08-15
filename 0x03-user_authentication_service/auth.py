#!/usr/bin/env python3
'''takes a password string argument and returns a bytes'''


import bcrypt


def _hash_password(password: str) -> bytes:
    '''take a string password and return a byte'''
    pass_str = password.encode('utf-8')
    salt = bcrypt.gensalt()
    pass_hash = bcrypt.hashpw(pass_str, salt)
    return pass_hash
