from flask import Blueprint, render_template

""" Define that this file is a blueprint of our application which means it has a bunch of routes inside (urls) """
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")
