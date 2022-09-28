"""Create your test for the user views here."""
import pytest
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.test import RequestFactory
from django.urls import reverse
from pytest_mock import MockFixture

from onebarangay_psql.users.factories import UserFactory
from onebarangay_psql.users.forms import UserAdminChangeForm
from onebarangay_psql.users.models import User
from onebarangay_psql.users.views import (
    UserRedirectView,
    UserUpdateView,
    user_detail_view,
)

pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """Test the user update view.

    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    @staticmethod
    def dummy_get_response(request: HttpRequest) -> None:
        """Get response dummy function.

        Args:
            request (HttpRequest): The request object.

        Returns:
            None: Returns None.
        """
        return None

    @staticmethod
    def test_get_success_url(user: User, rf: RequestFactory) -> None:
        """Test the UserUpdateView get_success_url method.

        Args:
            user (User): The user object.
            rf (RequestFactory): The request factory.
        """
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/users/{user.username}/"

    @staticmethod
    def test_get_object(user: User, rf: RequestFactory) -> None:
        """Test the UserUpdateView get_object method.

        Args:
            user (User): The user object.
            rf (RequestFactory): The request factory.
        """
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user

    @staticmethod
    def test_form_valid(user: User, rf: RequestFactory, mocker: MockFixture) -> None:
        """Test the UserUpdateView form_valid method.

        Args:
            user (User): The user object.
            rf (RequestFactory): The request factory.
        """
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        get_response = mocker.MagicMock(return_value=HttpResponse())

        # Add the session/message middleware to the request
        SessionMiddleware(get_response).process_request(request)
        MessageMiddleware(get_response).process_request(request)
        request.user = user

        view.request = request

        # Initialize the form
        form = UserAdminChangeForm()
        form.cleaned_data = {}
        view.form_valid(form)

        messages_sent = [m.message for m in messages.get_messages(request)]
        assert messages_sent == ["Information successfully updated"]


class TestUserRedirectView:
    """Test the user redirect view."""

    @staticmethod
    def test_get_redirect_url(user: User, rf: RequestFactory) -> None:
        """Test the UserRedirectView get_redirect_url method.

        Args:
            user:
            rf:
        """
        view = UserRedirectView()
        request = rf.get("/fake-url")
        request.user = user

        view.request = request

        assert view.get_redirect_url() == f"/users/{user.username}/"


class TestUserDetailView:
    """Test user detail view."""

    @staticmethod
    def test_authenticated(user: User, rf: RequestFactory):
        """Test authenticated user."""
        request = rf.get("/fake-url/")
        request.user = UserFactory()

        response = user_detail_view(request, username=user.username)

        assert response.status_code == 200

    @staticmethod
    def test_not_authenticated(user: User, rf: RequestFactory):
        """Test not authenticated user."""
        request = rf.get("/fake-url/")
        request.user = AnonymousUser()

        response = user_detail_view(request, username=user.username)
        login_url = reverse(settings.LOGIN_URL)

        assert isinstance(response, HttpResponseRedirect)
        assert response.status_code == 302
        assert response.url == f"{login_url}?next=/fake-url/"
