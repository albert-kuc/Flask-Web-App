from flask import Blueprint

""" Define that this file is a blueprint of our application which means it has a bunch of routes inside (urls) """
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1>Test<h1>"
