from flask import Blueprint

bp = Blueprint("python_api", __name__)


@bp.route("/liveness")
def liveness():
    return {"liveness": True}
