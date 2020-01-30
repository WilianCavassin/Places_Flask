from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager 

#databases
#void SQLAlchemy type for further use, view auth.py
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    UPLOAD_FOLDER = 'static/images'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #import table user
    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    from .places import places as places_bp
    app.register_blueprint(places_bp)

    from .search import search as search_bp
    app.register_blueprint(search_bp)

    from .register import register as register_bp
    app.register_blueprint(register_bp)

    return app