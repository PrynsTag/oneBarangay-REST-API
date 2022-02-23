"""Create your statistics drf http methods tests here."""

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient


class TestStatisticsViewSetUrls:
    """Create your rbi drf http methods tests here."""

    @pytest.mark.parametrize(
        "url",
        [
            "api:mv-signup-list",
            "api:mv-total-list",
            "api:mv-appointment-list",
            "api:mv-signin-list",
            "api:mv-age-group-list",
            "api:mv-citizenship-list",
            "api:mv-civil-status-list",
            "api:mv-average-list",
            "api:mv-social-class-list",
            "api:mv-refresh-list",
        ],
    )
    def test_house_record_list(self, admin_api_client: APIClient, url: str):
        """Test house record list.

        Scenario:
            - As an admin user, I should be able to access the house record list
        Args:
            admin_api_client (APIClient): The admin api client making the get request
        """
        response: Response = admin_api_client.get(reverse(url))
        assert response.status_code == status.HTTP_200_OK
