import factory

from python_api import models
from python_api.database import session


class BaseSQLAlchemyModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "flush"


class UserFactory(BaseSQLAlchemyModelFactory):
    class Meta:
        model = models.User

        sqlalchemy_session = session
        sqlalchemy_session_persistence = "commit"

    username = factory.Faker("user_name")
