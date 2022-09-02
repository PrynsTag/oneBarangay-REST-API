"""Create your test for the DRF views."""
import pytest
from django.test import RequestFactory

from onebarangay_psql.users.api.views import ProfileViewSet, UserViewSet
from onebarangay_psql.users.models import User

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    """Test DRF UserViewSet View."""

    @staticmethod
    def test_get_queryset(user: User, rf: RequestFactory) -> None:
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

    @staticmethod
    def test_me(user: User, rf: RequestFactory) -> None:
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

        data = {
            "id": user.username,
            "url": f"http://testserver/api/user/{user.username}/",
        }

        assert set(data.items()).issubset(set(response.data.items()))

    class TestUserProfileViewSet:
        """Test xDRF ProfileViewSet View."""

        @staticmethod
        def test_get_queryset(user: User, rf: RequestFactory) -> None:
            """Test 'get_queryset' returns the requesting user profile is returned.

            Args:
                user (User): The user to test.
                rf (RequestFactory): The request factory.
            """
            view = ProfileViewSet()
            request = rf.get("/fake-url/")
            request.user = user

            view.request = request

            assert user.profile in view.get_queryset()

        @staticmethod
        def test_me(user: User, rf: RequestFactory) -> None:
            """Test 'me' view returns requesting authenticated user's profile.

            Args:
                user (User): The user to test.
                rf (RequestFactory): The request factory.
            """
            view = ProfileViewSet()
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

        @staticmethod
        def test_get_object(user: User, rf: RequestFactory):
            """Test 'get_object' method returns the requesting authenticated user's profile.

            Args:
                user (User): The user to test.
                rf (RequestFactory): The request factory.
            """
            view = ProfileViewSet()
            request = rf.get("/fake-url/")
            request.user = user

            view.request = request
            view.kwargs = {"username": user.username}

            assert user == view.get_object().user
