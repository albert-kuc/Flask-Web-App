from flask import Blueprint, render_template
from flask_login import login_required, current_user

""" Define that this file is a blueprint of our application which means it has a bunch of routes inside (urls) """
views = Blueprint('views', __name__)


@views.route('/')
@login_required  # with this decorator we cannot access home page without user logged in
def home():
    return render_template("home.html")
