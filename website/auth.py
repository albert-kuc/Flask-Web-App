from flask import Blueprint

""" Define that this file is a blueprint of our application which means it has a bunch of routes inside (urls) """
auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<p>Login</p>"


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up')
def sign_up():
    return "<p>Sign up</p>"
