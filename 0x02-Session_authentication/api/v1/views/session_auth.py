#!/usr/bin/env python3
""" Module doe session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def authenticate_user():
    '''authenticate a user'''
    e_mail = request.form.get('email')
    passwd = request.form.get('password')
    if e_mail is None:
        return jsonify({"error": "email missing"}), 400
    if passwd is None:
        return jsonify({"error": "password missing"}), 400
    # my_obj = User.load_from_file()
    my_search = User.search({"email": e_mail})
    if not my_search or my_search == []:
        return jsonify({"error": "no user found for this email"}), 404
    else:
        for users in my_search:
            if not users.is_valid_password(passwd):
                return jsonify({"error": "wrong password"}), 401
            else:
                from api.v1.app import auth
                userid = users.id
                sessionid = auth.create_session(userid)
                cookie_name = os.getenv('SESSION_NAME')
                my_user = users.to_json()
                resp = make_response(my_user)
                resp.set_cookie(cookie_name, sessionid)
            return (resp)


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    '''logout or delete session id'''
    from api.v1.app import auth
    delete = auth.destroy_session(request)
    if delete is False:
        abort(404)
    return jsonify({}), 200
