"""Create your swagger-ui test here."""
import pytest
from django.test import Client
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_swagger_accessible_by_admin(admin_client: Client) -> None:
    """Test swagger-ui is accessible by admin user.

    Args:
        admin_client (object): Django test client for admin user.
    """
    url = reverse("api-docs")
    response = admin_client.get(url)
    assert response.status_code == 200


def test_swagger_ui_not_accessible_by_normal_user(client: Client) -> None:
    """Test swagger-ui is not accessible by normal user.

    Args:
        client (Client): Django test client for normal user.
    """
    url = reverse("api-docs")
    response = client.get(url)
    assert response.status_code == 403
