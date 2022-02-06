"""Create your user and profile test models here."""
import pytest

from onebarangay_psql.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User) -> None:
    """Test the get_absolute_url method of the User model.

    Args:
        user (User): A user object.
    """
    assert user.get_absolute_url() == f"/users/{user.username}/"


def test_create_user_with_profile(user: User) -> None:
    """Test creating a user with profile automatically created.

    Args:
        user (User): A user object.
    """
    assert user.date_joined.date() == user.profile.created_at.date()


def test_create_user():
    """Test creating a user."""
    user = User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="testpassword",
    )
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.profile.pk
    assert user.check_password("testpassword")
