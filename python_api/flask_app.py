from typing import Type

from flask import Flask

from python_api.routes import bp


class Config(object):
    pass


def create_app(config_class: Type[Config] = Config) -> Flask:
    app = Flask(__name__)

    app.config.from_object(config_class)

    app.register_blueprint(bp)

    return app
