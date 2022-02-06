"""Create your test for the DRF views."""
import pytest
from django.test import RequestFactory

from onebarangay_psql.users.api.views import UserProfileViewSet, UserViewSet
from onebarangay_psql.users.models import User

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    """Test DRF UserViewSet View."""

    def test_get_queryset(self, user: User, rf: RequestFactory) -> None:
        """Test 'get_queryset' returns the requesting user is returned.

        Args:
            user (User): The user to test.
            rf (RequestFactory): The request factory.
        """
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    def test_me(self, user: User, rf: RequestFactory) -> None:
        """Test 'me' view returns requesting authenticated user.

        Args:
            user (User): The user to test.
            rf (RequestFactory): The request factory.
        """
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        response = view.me(request)

        assert response.data == {
            "username": user.username,
            "name": user.name,
            "url": f"http://testserver/api/user/{user.username}/",
        }

    class TestUserProfileViewSet:
        """Test xDRF UserProfileViewSet View."""

        def test_get_queryset(self, user: User, rf: RequestFactory) -> None:
            """Test 'get_queryset' returns the requesting user profile is returned.

            Args:
                user (User): The user to test.
                rf (RequestFactory): The request factory.
            """
            view = UserProfileViewSet()
            request = rf.get("/fake-url/")
            request.user = user

            view.request = request

            assert user.profile == view.get_queryset()

        def test_me(self, user: User, rf: RequestFactory) -> None:
            """Test 'me' view returns requesting authenticated user's profile.

            Args:
                user (User): The user to test.
                rf (RequestFactory): The request factory.
            """
            view = UserProfileViewSet()
            request = rf.get("/fake-url/")
            request.user = user

            view.request = request

            response = view.me(request)
            user_data = [
                ("username", user.username),
                ("email", user.email),
                ("user", f"http://testserver/api/profile/{user.username}/"),
            ]

            assert set(user_data).issubset(response.data.items())

        def test_get_object(self, user: User, rf: RequestFactory):
            """Test 'get_object' method returns the requesting authenticated user's profile.

            Args:
                user (User): The user to test.
                rf (RequestFactory): The request factory.
            """
            view = UserProfileViewSet()
            request = rf.get("/fake-url/")
            request.user = user

            view.request = request
            view.kwargs = {"username": user.username}

            assert user == view.get_object().user
