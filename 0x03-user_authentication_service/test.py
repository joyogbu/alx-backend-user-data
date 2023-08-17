#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth
my_db = DB()
sessid = '07b58ed3-2072-462d-aa72-515842add14e'
#email = "bob@bob.com"
#try:
sessid = '07b58ed3-2072-462d-aa72-515842add14e'
email = 'test@test.com'
hashed_password = "hashedPwd"
user = my_db.add_user(email, hashed_password)
try:
    #user = Auth().get_user_from_session_id(sessid)
    user = my_db.find_user_by(email=email)
    print(Auth().create_session(user.email))
    print(user.email)
    print(Auth().get_reset_password_token(email))
    #my_db.destroy_session(user.id)
except ValueError:
    print("not found")

