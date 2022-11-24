"""Create your test for the appointment DRF urls."""
import pytest
from django.urls import resolve, reverse

from onebarangay_psql.appointment.models import Appointment


pytestmark = pytest.mark.django_db


class TestAppointmentViewSetUrls:
    """Test DRF URls for AnnouncementViewSet."""

    @staticmethod
    def test_appointment_detail(appointment: Appointment):
        """Test appointment 'detail' drf url to reverse and resolve.

        Args:
            appointment (Appointment): Appointment object to test.
        """
        assert (
            reverse("api:appointment-detail", kwargs={"pk": appointment.pk})
            == f"/api/appointment/{appointment.pk}/"
        )
        assert (
            resolve(f"/api/appointment/{appointment.pk}/").view_name
            == "api:appointment-detail"
        )

    @staticmethod
    def test_appointment_list():
        """Test appointment 'list' drf url to reverse and resolve."""
        assert reverse("api:appointment-list") == "/api/appointment/"
        assert resolve("/api/appointment/").view_name == "api:appointment-list"
