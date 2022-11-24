"""Create your test for permissions."""
from datetime import datetime

import pytest
from _pytest.fixtures import FixtureRequest
from django.test.client import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from onebarangay_psql.users.models import User


pytestmark = pytest.mark.django_db


@pytest.mark.parametrize("url_name", ["api:user-me", "api:profile-me"])
class TestUserAndProfileMePermission:
    """Test for user and profile 'me' permission."""

    # pylint: disable=redefined-outer-name
    @pytest.mark.parametrize("user_type", ["user", "admin_user"], indirect=True)
    def test_user_me_admin_permission(
        self, api_client: APIClient, user_type: User, url_name: str
    ) -> None:
        """Test for user and profile 'me' admin and user permission.

        Args:
            api_client (APIClient): Django rest framework client.
            user_type (User): User model.
            url_name (str): URL name.
        """
        api_client.force_login(user_type)

        url = reverse(url_name)
        get_response = api_client.get(url)

        assert get_response.status_code == status.HTTP_200_OK

    @staticmethod
    def test_user_me_not_authenticated_permission(
        api_client: APIClient, url_name: str
    ) -> None:
        """Test for user and profile 'me' not authenticated permission.

        Args:
            api_client (APIClient): Django rest framework client.
            url_name (str): URL name.
        """
        url = reverse(url_name)

        response = api_client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.parametrize("url_name", ["api:user-list", "api:profile-list"])
class TestUserAndProfileListPermission:
    """Test permission for listing users and profiles."""

    @staticmethod
    def test_profile_list_admin_permission(admin_client: Client, url_name: str) -> None:
        """Test for profile list admin permission.

        Args:
            admin_user (User): Admin user model.
            admin_client (APIClient): Django rest framework client.
            url_name (str): URL name.
        """
        response = admin_client.get(reverse(url_name))

        assert response.status_code == status.HTTP_200_OK

    @staticmethod
    def test_user_and_profile_list_user_permission(
        client: Client, user: User, url_name: str
    ) -> None:
        """Test for user and profile list user permission.

        Args:
            client (Client): Django test client.
            user (User): User model.
            url_name (str): URL name.
        """
        client.force_login(user)
        response = client.get(reverse(url_name))

        assert response.status_code == status.HTTP_403_FORBIDDEN

    @staticmethod
    def test_user_and_profile_list_not_authenticated_permission(
        client: Client, url_name: str
    ) -> None:
        """Test for user and profile list not authenticated permission.

        Args:
            client (Client): Django test client.
            url_name (str): URL name.
        """
        response = client.get(reverse(url_name))
        assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.fixture()
def user_type(request: FixtureRequest, user: User, admin_user: User):
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


@pytest.mark.parametrize("url_name", ["api:user-detail", "api:profile-detail"])
class TestUserAndProfileDetailPermission:
    """Test user and profile detail permission."""

    # pylint: disable=redefined-outer-name
    @pytest.mark.parametrize("user_type", ["user", "admin_user"], indirect=True)
    def test_user_and_profile_detail_permission(
        self, api_client: APIClient, user_type: User, url_name: str
    ) -> None:
        """Test user and profile detail permission.

        Args:
            api_client (APIClient): Django rest framework client.
            user_type (User): User to test permission for.
            url_name (str): URL name to test.
        """
        api_client.force_authenticate(user_type)

        last_login_data = datetime.now()
        patch_data = {"last_login": last_login_data}
        put_data = {
            "last_login": last_login_data,
            "gender": user_type.profile.gender or "O",
            "civil_status": user_type.profile.civil_status,
        }
        user_data = {"username": user_type.username}
        url = reverse(url_name, kwargs=user_data)

        get_response = api_client.get(url)
        put_response = api_client.put(url, put_data | user_data)
        patch_response = api_client.patch(url, patch_data)

        date_format = "%A, %b %d, %Y %I:%M %p"
        date_data = datetime.strftime(last_login_data, date_format)

        if "user-detail" in url_name:
            # User Model
            assert date_data == put_response.data["last_login"]
            assert date_data == patch_response.data["last_login"]
        else:
            # Profile Model
            assert date_data == put_response.data["created_at"]
            assert date_data == patch_response.data["created_at"]

        assert get_response.status_code == status.HTTP_200_OK
        assert put_response.status_code == status.HTTP_200_OK
        assert patch_response.status_code == status.HTTP_200_OK

    @staticmethod
    def test_user_and_profile_detail_not_authenticated_permission(
        api_client: Client, user: User, url_name: str
    ) -> None:
        """Test user and profile detail permission.

        Args:
            api_client (APIClient): Django rest framework client.
            user (User): User to test permission for.
            url_name (str): URL name to test.
        """
        response = api_client.get(reverse(url_name, kwargs={"username": user.username}))
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @staticmethod
    def test_user_and_profile_detail_not_owner_permission(
        api_client: Client, user: User, url_name: str
    ) -> None:
        """Test user and profile detail not owner permission.

        Args:
            api_client (APIClient): Django rest framework client.
            user (User): User to test permission for.
            url_name (str): URL names to test.
        """
        new_user = User.objects.create_user("new_user", "test@example.com", "testpass")

        api_client.force_login(user)
        response = api_client.get(
            reverse(url_name, kwargs={"username": new_user.username})
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN
