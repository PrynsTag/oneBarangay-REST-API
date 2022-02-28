"""Create your test for the DRF urls."""
import pytest
from django.urls import resolve, reverse

from onebarangay_psql.users.models import User

pytestmark = pytest.mark.django_db


class TestUserViewSetUrls:
    """Test DRF URls for UserViewSet."""

    def test_user_detail(self, user: User):
        """Test user 'detail' drf url to reverse and resolve."""
        assert (
            reverse("api:user-detail", kwargs={"username": user.username})
            == f"/api/user/{user.username}/"
        )
        assert resolve(f"/api/user/{user.username}/").view_name == "api:user-detail"

    def test_user_list(self):
        """Test user 'list' drf url to reverse and resolve."""
        assert reverse("api:user-list") == "/api/user/"
        assert resolve("/api/user/").view_name == "api:user-list"

    def test_user_me(self):
        """Test user 'me' drf url to reverse and resolve."""
        assert reverse("api:user-me") == "/api/user/me/"
        assert resolve("/api/user/me/").view_name == "api:user-me"


class TestUserProfileViewSetUrls:
    """Test DRF URls for ProfileViewSet."""

    def test_profile_detail(self, user: User):
        """Test profile 'detail' drf url to reverse and resolve.

        Args:
            user (User): User object.
        """
        assert (
            reverse("api:profile-detail", kwargs={"username": user.username})
            == f"/api/profile/{user.username}/"
        )
        assert (
            resolve(f"/api/profile/{user.username}/").view_name == "api:profile-detail"
        )

    def test_profile_list(self):
        """Test profile 'list' drf url to reverse and resolve."""
        assert reverse("api:profile-list") == "/api/profile/"
        assert resolve("/api/profile/").view_name == "api:profile-list"

    def test_profile_me(self):
        """Test profile 'me' drf url to reverse and resolve."""
        assert reverse("api:profile-me") == "/api/profile/me/"
        assert resolve("/api/profile/me/").view_name == "api:profile-me"
