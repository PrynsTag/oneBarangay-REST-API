"""Create your appointment model tests here."""
import zoneinfo
from datetime import datetime, timedelta

import pytest

from onebarangay_psql.appointment.models import Appointment
from onebarangay_psql.users.models import User


pytestmark = pytest.mark.django_db


class TestAppointment:
    """Test the Appointment model."""

    @staticmethod
    def test_create_appointment(admin_user: User) -> None:
        """Test creating an announcement.

        Args:
            admin_user (User): The admin user creating the appointment.
        """
        a1 = Appointment.objects.create(
            recipient_name=f"{admin_user.profile.first_name} {admin_user.profile.last_name}",
            purpose="Test Purpose",
            user=admin_user,
            start_appointment=datetime.now(tz=zoneinfo.ZoneInfo("Asia/Manila")),
            document="IND",
            government_id="appointment/government_id/default.png",
        )

        assert a1.purpose == "Test Purpose"
        assert a1.user == admin_user
        assert a1.document == "IND"

    @staticmethod
    def test_str(admin_user: User) -> None:
        """Test the string representation of an appointment.

        Args:
            admin_user (User): The admin user creating the appointment.
        """
        a1 = Appointment.objects.create(
            recipient_name=f"{admin_user.profile.first_name} {admin_user.profile.last_name}",
            purpose="Test Purpose",
            user=admin_user,
            start_appointment=datetime.now(tz=zoneinfo.ZoneInfo("Asia/Manila")),
            document="IND",
            government_id="appointment/government_id/default.png",
        )

        assert str(a1) == f"{a1.user} - {a1.purpose}"

    @staticmethod
    def test_update_appointment(admin_user: User) -> None:
        """Test updating an appointment.

        Args:
            admin_user (User): The admin user creating the appointment.
        """
        a1 = Appointment.objects.create(
            recipient_name=f"{admin_user.profile.first_name} {admin_user.profile.last_name}",
            purpose="Test Purpose",
            user=admin_user,
            start_appointment=datetime.now(tz=zoneinfo.ZoneInfo("Asia/Manila")),
            document="IND",
            government_id="appointment/government_id/default.png",
        )
        updated_appointment = a1.start_appointment + timedelta(days=1)
        a1.start_appointment = updated_appointment
        a1.save()

        assert a1.start_appointment == updated_appointment

    @staticmethod
    def test_appointment_ordering(admin_user: User) -> None:
        """Test the ordering of appointment.

        The most recent announcement should be first.
        Args:
            admin_user (User): The admin user creating the appointment.
        """
        Appointment.objects.create(
            recipient_name=f"{admin_user.profile.first_name} {admin_user.profile.last_name}",
            purpose="Test Purpose 1",
            user=admin_user,
            start_appointment=datetime.now(tz=zoneinfo.ZoneInfo("Asia/Manila")),
            document="IND",
            government_id="appointment/government_id/default.png",
        )

        Appointment.objects.create(
            recipient_name=f"{admin_user.profile.first_name} {admin_user.profile.last_name}",
            purpose="Test Purpose 2",
            user=admin_user,
            start_appointment=datetime.now(tz=zoneinfo.ZoneInfo("Asia/Manila")),
            document="IND",
            government_id="appointment/government_id/default.png",
        )
        appointment = Appointment.objects.all()
        assert appointment[0].purpose == "Test Purpose 1"
        assert appointment[1].purpose == "Test Purpose 2"
