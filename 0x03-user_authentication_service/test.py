#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User


my_db = DB()
sessid = 'a8a2cf90-1579-432f-ad98-b15c3cfacde1'
email = "bob@bob.com"
user = my_db.find_user_by(email=email)
print (user)
