from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

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

@views.route('/delete-note', methods=['POST'])
def delete_note():
    """
    Take in data from post request and load as json object, access note_id attribute, look up Note with that id,
    if Note exists and current user owns this Note, delete it. Return an empty response.
    """
    note = json.loads(request.data)
    note_id = note['note_id']
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})