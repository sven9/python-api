import pytest

from python_api.exceptions import RepositoryException
from python_api.models import User
from python_api.repositories import user_repository
from tests.factories import UserFactory


class TestUserRepository:
    def test_it_finds_a_user_by_id(self):
        user = UserFactory.create()

        found_user = user_repository.find_by_id(user.id)

        assert found_user.username == user.username

    def test_it_raises_exception_for_user_not_found(self):
        user = UserFactory.create(is_deleted=True)

        with pytest.raises(RepositoryException):
            user_repository.find_by_id(user.id)

    def test_it_creates_a_user(self, database):
        user = UserFactory.build()

        user_repository.create(user)

        created_user = database.query(User).get(user.id)

        assert created_user.username == user.username

    def test_it_updates_a_user(self, faker, database):
        user = UserFactory.create()
        new_username = faker.user_name()

        user.username = new_username
        user_repository.update(user)

        updated_user = database.query(User).get(user.id)

        assert updated_user.username == user.username

    def test_it_deletes_a_user(self, database):
        user = UserFactory.create()

        user_repository.delete(user)

        deleted_user = database.query(User).get(user.id)

        assert deleted_user.is_deleted
        assert deleted_user.deleted_on is not None
