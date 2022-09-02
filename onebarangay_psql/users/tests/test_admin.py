"""Create your tests for the admin app here."""
import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

pytestmark = pytest.mark.django_db
User = get_user_model()


class TestUserAdmin:
    """Test the admin interface."""

    @staticmethod
    def test_changelist(admin_client):
        """Test the changelist view."""
        url = reverse("admin:users_user_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    @staticmethod
    def test_search(admin_client):
        """Test the search functionality."""
        url = reverse("admin:users_user_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    @staticmethod
    def test_add(admin_client):
        """Test the add user functionality."""
        url = reverse("admin:users_user_add")
        response = admin_client.get(url)
        assert response.status_code == 200

    @staticmethod
    def test_view_user(admin_client):
        """Test the view user functionality."""
        user = User.objects.get(username="admin")
        url = reverse("admin:users_user_change", kwargs={"object_id": user.pk})
        response = admin_client.get(url)
        assert response.status_code == 200
