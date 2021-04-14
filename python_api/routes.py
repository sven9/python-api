from flasgger import swag_from
from flask import Blueprint

from python_api.openapi import FLASGGER_DIR
from python_api.schemas import LivenessSchema

bp = Blueprint("python_api", __name__)


@bp.route("/liveness")
@swag_from(FLASGGER_DIR / "liveness.yml", methods=["GET"])
def liveness():
    schema = LivenessSchema()

    return schema.dump({"liveness": True})
