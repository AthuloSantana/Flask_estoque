from flask import Flask

import views
from ext import config, database


def init_app():
    app = Flask(__name__)

    config.init_app(app)
    database.init_app(app)
    views.init_app(app)

    return app
