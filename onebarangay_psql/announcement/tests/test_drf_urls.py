"""Create your test for the DRF urls."""
import pytest
from django.urls import resolve, reverse

from onebarangay_psql.announcement.models import Announcement

pytestmark = pytest.mark.django_db


class TestAnnouncementViewSetUrls:
    """Test DRF URls for AnnouncementViewSet."""

    def test_announcement_detail(self, announcement: Announcement):
        """Test announcement 'detail' drf url to reverse and resolve.

        Args:
            announcement (Announcement): Announcement object.
        """
        assert (
            reverse("api:announcement-detail", kwargs={"slug": announcement.slug})
            == f"/api/announcement/{announcement.slug}/"
        )
        assert (
            resolve(f"/api/announcement/{announcement.slug}/").view_name
            == "api:announcement-detail"
        )

    def test_announcement_list(self):
        """Test announcement 'list' drf url to reverse and resolve."""
        assert reverse("api:announcement-list") == "/api/announcement/"
        assert resolve("/api/announcement/").view_name == "api:announcement-list"
