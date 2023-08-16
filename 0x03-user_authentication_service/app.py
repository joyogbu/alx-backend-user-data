#!/usr/bin/env python3
'''create a basic flask app'''


from flask import Flask, jsonify, request, abort, make_response
from user import User
from db import DB
from auth import Auth


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
    # user = AUTH.find_user_by(email=email)
    login_valid = AUTH.valid_login(email, passwd)
    if login_valid is False:
        abort(401)
    sessionid = AUTH.create_session(email)
    resp = make_response(sessionid)
    resp.set_cookie('session_id', sessionid)
    return jsonify({"email": email, "message": "logged in"})


# AUTH = Auth()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
