"""Create your statistics drf urls tests here."""
import pytest
from django.urls import resolve, reverse


class TestStatisticsViewSetUrls:
    """Test StatisticsViewSet urls."""

    @pytest.mark.parametrize(
        ("app_url", "url_path"),
        [
            ("api:mv-signup-list", "/api/statistics/user-signup/"),
            ("api:mv-total-list", "/api/statistics/totals/"),
            ("api:mv-appointment-list", "/api/statistics/appointment/"),
            ("api:mv-signin-list", "/api/statistics/user-login/"),
            ("api:mv-age-group-list", "/api/statistics/age-group/"),
            ("api:mv-citizenship-list", "/api/statistics/citizenship/"),
            ("api:mv-civil-status-list", "/api/statistics/civil-status/"),
            ("api:mv-average-list", "/api/statistics/average/"),
            ("api:mv-social-class-list", "/api/statistics/social-class/"),
            ("api:mv-refresh-list", "/api/statistics/refresh/"),
        ],
    )
    def test_statistics_list(self, app_url: str, url_path: str):
        """Test statistics list url."""
        assert reverse(app_url) == url_path
        assert resolve(url_path).view_name == app_url
