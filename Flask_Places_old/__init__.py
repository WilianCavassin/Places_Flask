from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager 
from flask_oauth import 
db = SQLAlchemy()

#facebook data
FB_APP_ID = '618193602247857'
FB_APP_SECRET = '8913302f03aac9764a1f135051eac3a8'
FB_AUTHORIZATION_BASE_URL = 'https://www.facebook.com/dialog/oauth'
FB_TOKEN_URL = "https://graph.facebook.com/oauth/access_token"
FB_


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app