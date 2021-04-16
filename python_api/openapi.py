from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flasgger import APISpec, Swagger
from flask import Flask

from python_api import PROJECT_DIR, __version__
from python_api.schemas import HealthCheckSchema, LivenessSchema

FLASGGER_DIR = PROJECT_DIR / "spec"


def configure_openapi_with_flask(app: Flask):
    spec = APISpec(
        title="Python API",  # noqa
        version=__version__,  # noqa
        openapi_version="2.0",  # noqa
        plugins=[  # noqa
            FlaskPlugin(),
            MarshmallowPlugin(),
        ],
    )

    template = spec.to_flasgger(
        app,
        definitions=[
            LivenessSchema,
            HealthCheckSchema,
        ],
    )

    Swagger(app, template=template)
