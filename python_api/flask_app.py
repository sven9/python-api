import logging
from typing import Type

from flask import Flask

from python_api.openapi import configure_openapi_with_flask
from python_api.routes import bp

logging.getLogger("werkzeug").propagate = False  # Prevents duplicate access logs during development


class Config(object):
    pass


def create_app(config_class: Type[Config] = Config) -> Flask:
    app = Flask(__name__)

    app.config.from_object(config_class)

    app.register_blueprint(bp)

    configure_openapi_with_flask(app)

    return app
