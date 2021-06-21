from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

""" Define that this file is a blueprint of our application which means it has a bunch of routes inside (urls) """
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required  # with this decorator we cannot access home page without user logged in
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    # reference a current user in base template and check if it's authenticated
    return render_template("home.html", user=current_user)
