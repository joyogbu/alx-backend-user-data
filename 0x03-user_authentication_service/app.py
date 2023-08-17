#!/usr/bin/env python3
'''create a basic flask app'''


from flask import Flask, jsonify, request, abort, make_response
from flask import url_for, redirect
from user import User
from db import DB
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)

AUTH = Auth()
@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    '''return a single payload'''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    '''register a new user'''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError as err:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    '''login a user and create a session id'''
    email = request.form.get('email')
    passwd = request.form.get('password')
    # user = DB.find_user_by(email=email)
    login_valid = AUTH.valid_login(email, passwd)
    if login_valid is False:
        abort(401)
    sessionid = AUTH.create_session(email)
    out = jsonify({"email": email, "message": "logged in"})
    out.set_cookie('session_id', sessionid)
    return out


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    '''logout and destroy session'''
    sessid = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(sessid)
    if user is not None:
        destroy_session(user.id)
        redirect(url_for('index'))
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    '''implementing the user profile'''
    sessid = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(sessid)
    if user is not None:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    '''get reset password token'''
    email = request.form.get('email')
    try:
        tok = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": tok}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    '''update the password'''
    email = request.form.get("email")
    reset_token = request.form.get('reset_token')
    passwd = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, passwd)
        return jsonify({"email": email, "message": "password updated"})
    except ValueError:
        abort(403)

# AUTH = Auth()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
