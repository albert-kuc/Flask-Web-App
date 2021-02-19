from flask import Flask


# Setup flask application
def create_app():
    app = Flask(__name__)  # initialize app
    # encrypt or secure cookies and session data related to the website
    app.config['SECRET_KEY'] = 'lkxauqeyd gpiwfpos quw'

    # tell flask we have some blueprints containing URLs for the application
    from .views import views
    from .auth import auth

    # register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
