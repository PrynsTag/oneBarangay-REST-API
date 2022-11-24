"""Create your test for user urls."""
import pytest
from django.urls import resolve, reverse

from onebarangay_psql.users.models import User


pytestmark = pytest.mark.django_db


def test_detail(user: User) -> None:
    """Test user detail url.

    Args:
        user (User): User object.
    """
    assert (
        reverse("users:detail", kwargs={"username": user.username})
        == f"/users/{user.username}/"
    )
    assert resolve(f"/users/{user.username}/").view_name == "users:detail"


def test_update() -> None:
    """Test user update url."""
    assert reverse("users:update") == "/users/~update/"
    assert resolve("/users/~update/").view_name == "users:update"


def test_redirect() -> None:
    """Test user redirect url."""
    assert reverse("users:redirect") == "/users/~redirect/"
    assert resolve("/users/~redirect/").view_name == "users:redirect"
