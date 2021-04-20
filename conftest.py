import pytest

from python_api.database import engine, session
from python_api.models import Base


@pytest.fixture(autouse=True)
def database():
    Base.metadata.create_all(engine)

    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)
