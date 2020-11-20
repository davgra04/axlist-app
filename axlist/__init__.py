import os

from flask import Flask, request

import datetime as dt


def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "auxcord.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db

    db.init_app(app)

    @app.before_request
    def add_to_access_list():
        ts = dt.datetime.now()

        ip = request.remote_addr
        if "X-Real-Ip" in request.headers:
            ip = request.headers["X-Real-Ip"]

        # headers_list = request.headers.getlist("X-Forwarded-For")
        # ip = headers_list[0] if headers_list else request.remote_addr

        print("HEYO BOYO")

        database = db.get_db()
        database.execute(
            "INSERT INTO accesslist (ts, ip, method, path) VALUES (?, ?, ?, ?)",
            (ts, ip, request.method, request.path),
        )
        database.commit()


    from . import accesslist

    app.register_blueprint(accesslist.bp)
    app.add_url_rule("/", endpoint="index")
    app.add_url_rule("/debug", endpoint="debug")

    return app
