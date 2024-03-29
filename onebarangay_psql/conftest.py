"""Universal settings for tests."""

import pytest
from _pytest.tmpdir import TempPathFactory
from pytest_django.fixtures import SettingsWrapper
from rest_framework.test import APIClient

from onebarangay_psql.announcement import models
from onebarangay_psql.announcement.factories import AnnouncementFactory
from onebarangay_psql.appointment.factories import AppointmentFactory
from onebarangay_psql.appointment.models import Appointment
from onebarangay_psql.rbi.factories import FamilyMemberFactory, HouseRecordFactory
from onebarangay_psql.rbi.models import FamilyMember, HouseRecord
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
    client.force_login(user)
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
    client.force_login(admin_user)
    return client


@pytest.fixture(autouse=True)
def announcement() -> models.Announcement:
    """Announcement factory for creating announcements.

    Returns:
        (Announcement): Announcement object
    """
    return AnnouncementFactory()


@pytest.fixture()
def appointment() -> Appointment:
    """Appointment factory for creating dummy appointments.

    Returns:
        (Appointment): The dummy appointment object
    """
    return AppointmentFactory()


@pytest.fixture()
def house_record() -> HouseRecord:
    """House record factory for creating dummy house records.

    Returns:
        (HouseRecord): The dummy house record object
    """
    return HouseRecordFactory()


@pytest.fixture()
def family_member() -> FamilyMember:
    """Family member factory for creating dummy family member.

    Returns:
        (FamilyMember): The dummy family member object
    """
    return FamilyMemberFactory()


@pytest.fixture()
def user_type(request, user: User, admin_user: User):
    """Return different user type.

    Args:
        request (pytest.fixture): pytest fixture.
        user (User): User object.
        admin_user (User): Admin user object.

    Returns:
        User: User object.
    """
    if request.param == "user":
        return user
    return admin_user
