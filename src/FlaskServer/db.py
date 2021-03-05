from src.DatabaseDriver.db_client import MongoDatabaseDriverProduction, MongoDatabaseDriverDevelop
from flask import current_app, g


"""
g is a special object that is unique for each request. 
It is used to store data that might be accessed by multiple functions during the request. 
The connection is stored and reused instead of creating a new connection if get_db is called
a second time in the same request."""


def get_db():
    if 'db' not in g:
        version = {
            "develop": MongoDatabaseDriverDevelop(uri=current_app.config["URI"]),
            "production": MongoDatabaseDriverProduction(uri=current_app.config["URI"])
        }
        g.db = version[current_app.config["DB_MODE"]]
    return g.db


def close_db(e=None):
    db = g.pop('db', None)  # remove the db instance from g and return it to a variable

    if db is not None:  # if db exists the connection is closed.
        db.client.close()


def init_app(app):
    app.teardown_appcontext(close_db)  # trigger the close_db method after resolving the request.
