import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TimestampMixin(object):
    created_on = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class SoftDeleteMixin(object):
    is_deleted = Column(Boolean, nullable=False, default=False)
    deleted_on = Column(DateTime, nullable=True)


class User(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)


class HealthCheck:
    is_healthy: bool
    dependencies: dict

    def __init__(self, is_database_healthy: bool):
        self.dependencies = {
            "is_database_healthy": is_database_healthy,
        }

        self.is_healthy = is_database_healthy
