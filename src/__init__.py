import os

from flask import Flask, g
from tinydb import TinyDB


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    db = TinyDB("db.json")

    try:
        os.makedirs(app.instance_path)
    except OSError as err:
        if err.errno == 17:
            print("Instance folder already exists.")
        else:
            raise Exception("Couldn't create instance folder.")

    app.config.from_mapping(
        SECRET_KEY="12345678", DATABASE=os.path.join(app.instance_path, "database.db")
    )

    with app.app_context():
        from .routes.routes import main_bp

        app.register_blueprint(main_bp)

    return app
