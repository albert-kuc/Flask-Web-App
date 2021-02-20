from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# define a new database
db = SQLAlchemy()
# specify database name
DB_NAME = "database.db"


# Setup flask application
def create_app():
    app = Flask(__name__)  # initialize app
    # encrypt or secure cookies and session data related to the website
    app.config['SECRET_KEY'] = 'lkxauqeyd gpiwfpos quw'
    # point to flask where sql database is located
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initialize database
    db.init_app(app)

    # tell flask we have some blueprints containing URLs for the application
    from .views import views
    from .auth import auth

    # register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # run models file to define User, Note classes before we initialize a database
    from .models import User, Note

    create_database(app)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
