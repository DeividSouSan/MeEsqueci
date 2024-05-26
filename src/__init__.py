import os
import sqlite3

from flask import Flask, g
from flask_bootstrap import Bootstrap5

bootstrap = Bootstrap5()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    bootstrap.init_app(app)
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

    # todo: Colocar esses métodos do banco de dados em uma classe ou arquivo diferente
    def get_db():
        if "db" not in g:
            g.db = sqlite3.connect(
                app.config["DATABASE"],
            )

        return g.db

    @app.teardown_appcontext
    def close_db(exception):
        db = g.pop("db", None)

        if db is not None:
            db.close()

    # todo: recriar o banco de dados pois adicionei o status 4 depois de ter criado o bd
    def init_db():
        db = get_db()
        db.executescript(
            """
            CREATE TABLE IF NOT EXISTS Categories (
                idCategory INTEGER NOT NULL,
                name TEXT NOT NULL,
                PRIMARY KEY(idCategory)
            );


            CREATE TABLE IF NOT EXISTS Items (
                idItem INTEGER NOT NULL,
                name TEXT NOT NULL,
                status INTEGER NOT NULL,

                PRIMARY KEY(idItem)
                CHECK(status IN (1, 2, 3, 4))
            );"""
        )

    with app.app_context():
        init_db()

        from .routes.routes import main_bp

        app.register_blueprint(main_bp)

    return app
