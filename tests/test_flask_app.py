from http import HTTPStatus

import pytest

from python_api.flask_app import Config, create_app


class TestConfig(Config):
    TESTING = True


flask_app = create_app(TestConfig)


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


def test_liveness_route(client):
    response = client.get("/liveness")

    assert response.status_code == HTTPStatus.OK
    assert response.json["liveness"]


def test_health_check_route(client):
    response = client.get("/health")

    assert response.status_code == HTTPStatus.OK
    assert response.json["is_healthy"]
    assert response.json["dependencies"]["is_database_healthy"]
