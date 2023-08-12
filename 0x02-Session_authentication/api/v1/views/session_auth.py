#!/usr/bin/env python3
""" Module doe session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def authenticate_user():
    '''authenticate a user'''
    email = request.form.get('email')
    passwd = request.form.get('password')
    if email is None:
        return jsonify({"error": "email missing"}), 400
    if passwd is None:
        return jsonify({"error": "password missing"}), 400
    # my_obj = User.load_from_file()
    my_search = User.search({"email": email})
    if not my_search:
        return jsonify({"error": "no user found for this email"}), 404
    if not User().is_valid_password(passwd):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    sessionid = auth.create_session()
    cookie_name = os.getenv('SESSION_NAME')
    my_user = User.to_json(my_search)
    my_user.set_cookie(cookie_name, my_search)
    return my_user
