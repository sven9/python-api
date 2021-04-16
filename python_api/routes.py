from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint

from python_api.openapi import FLASGGER_DIR
from python_api.queries import HealthCheckQuery
from python_api.schemas import HealthCheckSchema, LivenessSchema

bp = Blueprint("python_api", __name__)


@bp.route("/liveness")
@swag_from(FLASGGER_DIR / "liveness.yml", methods=["GET"])
def liveness():
    schema = LivenessSchema()

    return schema.dump({"liveness": True})


@bp.route("/health")
@swag_from(FLASGGER_DIR / "health_check.yml", methods=["GET"])
def health():
    health_check = HealthCheckQuery.check_health()

    schema = HealthCheckSchema()

    response_code = HTTPStatus.OK if health_check.is_healthy else HTTPStatus.INTERNAL_SERVER_ERROR

    return schema.dump(health_check), response_code
