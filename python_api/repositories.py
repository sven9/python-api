import datetime
from abc import ABC, abstractmethod

from sqlalchemy.orm.exc import NoResultFound

from python_api.database import session
from python_api.exceptions import RepositoryException
from python_api.models import User


class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, ident: int) -> User:
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user: User):
        pass


class UserRepositorySqlAlchemyAdapter(UserRepository):
    def find_by_id(self, ident: int) -> User:
        try:
            return session.query(User).filter(User.id == ident, User.is_deleted == False).one()  # noqa
        except NoResultFound:
            raise RepositoryException(f"`user` record not found for id: {ident}")

    def find_by_username(self, username: str) -> User:
        try:
            return session.query(User).filter(User.username == username, User.is_deleted == False).one()  # noqa
        except NoResultFound:
            raise RepositoryException(f"`user` record not found for username: {username}")

    def create(self, user: User) -> User:
        session.add(user)
        session.commit()

        return user

    def update(self, user: User) -> User:
        session.commit()

        return user

    def delete(self, user: User):
        user.is_deleted = True
        user.deleted_on = datetime.datetime.utcnow()

        session.commit()

        return user


user_repository = UserRepositorySqlAlchemyAdapter()
