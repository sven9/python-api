import logging
import os
from typing import Type

import json_logging
from flask import Flask

from python_api.database import Session
from python_api.openapi import configure_openapi_with_flask
from python_api.routes import bp

logging.getLogger("werkzeug").propagate = False  # Prevents duplicate access logs during development


class Config(object):
    pass


def create_app(config_class: Type[Config] = Config) -> Flask:
    app = Flask(__name__)

    if os.environ["FLASK_ENV"] == "production":
        json_logging.init_flask(enable_json=True)
        json_logging.init_request_instrument(app)

    app.config.from_object(config_class)

    app.register_blueprint(bp)

    configure_openapi_with_flask(app)

    @app.teardown_appcontext
    def cleanup(resp_or_exc):
        Session.remove()

    return app
