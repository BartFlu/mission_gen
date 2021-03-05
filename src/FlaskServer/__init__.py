from flask import Flask
import os
from dacite import from_dict
from .Config import ConfigDevelop, ConfigProduction


def create_app():
    # create and configure the app
    app = Flask(__name__)
    if not os.environ.get('DB_Mode'):
        app.config.from_object(ConfigDevelop())

    elif os.environ.get('DB_MODE'):
        app.config.from_object(ConfigProduction())

    from src.FlaskServer import db
    db.init_app(app)

    from src.FlaskServer.auth import auth
    app.register_blueprint(auth)

    from src.FlaskServer.json_output import json_output_component
    app.register_blueprint(json_output_component)

    from src.FlaskServer.html_output import html_output_component
    app.register_blueprint(html_output_component)

    from src.FlaskServer.contact_terrain import b_contact_terrain
    app.register_blueprint(b_contact_terrain)

    from flask_admin import Admin
    admin = Admin(app)
    from src.DataModel.mission_model import MissionView
    from src.DataModel.usermodel import UserView
    with app.app_context():  # create app context required by flask g. Necessary to run add_view in the factory method.
        admin.add_view(UserView(db.get_db().db['users']))
        admin.add_view(MissionView(db.get_db().db['missions']))

    from flask_login import LoginManager
    from src.DataModel.usermodel import User
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(username):
        d_b = db.get_db()
        u = d_b.user_driver.get_user_by_username(username)

        if not u:
            print('User loader returned None')
            return None
        user = from_dict(data_class=User, data=u)
        print(f'User loader returned{user}')
        return user

    return app


if __name__ == '__main__':
    create_app()
