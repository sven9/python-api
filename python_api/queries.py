from sqlalchemy.exc import SQLAlchemyError

from python_api import logger
from python_api.database import session
from python_api.models import HealthCheck, User
from python_api.repositories import user_repository
from python_api.schemas import HealthCheckSchema


class HealthCheckQuery:
    @classmethod
    def check_health(cls):
        health_check = HealthCheck(is_database_healthy=cls.check_database())

        if not health_check.is_healthy:
            schema = HealthCheckSchema()
            logger.fatal({"HealthCheck": schema.dump(health_check)})

        return health_check

    @classmethod
    def check_database(cls):
        try:
            session.execute("SELECT 1").one()
        except SQLAlchemyError as e:
            logger.exception(e)

            return False

        return True


class UserQuery:
    @classmethod
    def find_by_username(cls, username: str) -> User:
        return user_repository.find_by_username(username)
