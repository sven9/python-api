from flask import Blueprint

from python_api.schema import LivenessSchema

bp = Blueprint("python_api", __name__)


@bp.route("/liveness")
def liveness():
    schema = LivenessSchema()

    return schema.dump({"liveness": True})
