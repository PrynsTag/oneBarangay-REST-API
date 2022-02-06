"""Universal settings for tests."""

import pytest
from _pytest.tmpdir import TempPathFactory
from pytest_django.fixtures import SettingsWrapper
from rest_framework.test import APIClient

from onebarangay_psql.users.factories import UserFactory
from onebarangay_psql.users.models import User


@pytest.fixture(autouse=True)
def _media_storage(settings: SettingsWrapper, tmpdir: TempPathFactory) -> None:
    """Temporary media storage for file upload testing.

    Args:
        settings:
        tmpdir:
    """
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture(autouse=True)
def user() -> User:
    """User Factory for creating a user.

    Returns:
        User (User): A user.
    """
    return UserFactory()


@pytest.fixture(autouse=True)
def api_client() -> APIClient:
    """Create an API client.

    Returns:
        APIClient (APIClient): An API client.
    """
    return APIClient()


# pylint: disable=redefined-outer-name
@pytest.fixture(autouse=True)
def user_api_client(user: User) -> APIClient:
    """User API client.

    Args:
        user (User): A user to log in with.

    Returns:
        APIClient (APIClient): An API client.
    """
    client = APIClient()
    client.login(username=user.username, password=user.password)
    return client


@pytest.fixture(autouse=True)
def admin_api_client(admin_user: User) -> APIClient:
    """Admin API client.

    Args:
        admin_user (User): An admin user to log in with.

    Returns:
        APIClient (APIClient): An API client.
    """
    client = APIClient()
    client.login(username=admin_user.username, password=admin_user.password)
    return client
