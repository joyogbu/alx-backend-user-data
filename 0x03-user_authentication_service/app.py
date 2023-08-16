#!/usr/bin/env python3
'''create a basic flask app'''


from flask import Flask, jsonify, request
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


# AUTH = Auth()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
