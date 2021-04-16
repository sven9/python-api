from sqlalchemy.exc import SQLAlchemyError

from python_api import logger
from python_api.database import session
from python_api.models import HealthCheck


class HealthCheckQuery:
    @classmethod
    def check_health(cls):
        health_check = HealthCheck(is_database_healthy=cls.check_database())

        return health_check

    @classmethod
    def check_database(cls):
        try:
            session.execute("SELECT 1").one()
        except SQLAlchemyError as e:
            logger.exception(e)

            return False

        return True
