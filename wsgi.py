import os

if os.environ["FLASK_ENV"] == "production":
    from gevent import monkey  # noqa

    monkey.patch_all()

from python_api.flask_app import create_app

app = create_app()
