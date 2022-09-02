"""Create your appointment drf http methods tests here."""
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test.client import Client
from django.urls import reverse
from rest_framework import status

from config.settings.base import APPS_DIR
from onebarangay_psql.appointment.models import Appointment

User = get_user_model()


# mypy: ignore-errors
class TestAppointmentViewSetUrls:
    """Test AppointmentViewSet URLs."""

    @pytest.mark.parametrize(
        ("user_type", "status_code"),
        [("admin", status.HTTP_200_OK), ("user", status.HTTP_403_FORBIDDEN)],
    )
    def test_appointment_list_url(
        self,
        user_type: str,
        status_code: int,
        user: User,
        admin_user: User,
        api_client: Client,
    ) -> None:
        """Test the appointment list url.

        Scenario:
            - As an admin user, I should be able to access the appointment list url.
            - As a user, I should not be able to access the appointment list url.
        Args:
            user_type (User): The user that accesses the URL.
            status_code (int): The expected status code.
            user (User): The user that accesses the URL.
            admin_user (User): The admin user that accesses the URL.
            api_client (Client): The api client.
        """
        logged_user = admin_user if user_type == "admin" else user
        api_client.force_login(logged_user)

        response = api_client.get(reverse("api:appointment-list"))
        assert response.status_code == status_code

    @pytest.mark.parametrize("user_type", ["admin", "user"], indirect=True)
    def test_appointment_retrieve_url(
        self, user_type: User, api_client: Client
    ) -> None:
        """Test the appointment retrieve url.

        Scenario:
            - As a user or admin, I should be able to access the appointment retrieve url.
        Args:
            user_type (User): The user that accesses the URL.
            api_client (Client): The api client.
        """
        api_client.force_login(user_type)

        a1 = Appointment.objects.create(
            recipient_name=f"{user_type.first_name} {user_type.last_name}",
            purpose="Test Appointment",
            start_appointment=datetime.now(tz=ZoneInfo("Asia/Manila")),
            document="IND",
            user=user_type,
        )
        response = api_client.get(
            reverse("api:appointment-detail", kwargs={"pk": a1.id})
        )

        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.parametrize("user_type", ["admin", "user"], indirect=True)
    def test_appointment_create_url(self, user_type: User, api_client: Client) -> None:
        """Test the appointment create url.

        Scenario:
            - As a user or admin, I should be able to create an appointment.
        Args:
            api_client (Client): The api client that sends the post request.
        """
        api_client.force_login(user_type)

        with open(APPS_DIR / "media/appointment/government_id/default.png", "rb") as f:
            image = SimpleUploadedFile(f.name, f.read(), content_type="image/jpeg")

        response = api_client.post(
            reverse("api:appointment-list"),
            {
                "recipient_name": "Prince Velasco",
                "purpose": "Test Appointment",
                "start_appointment": datetime.now(tz=ZoneInfo("Asia/Manila")),
                "document": "IND",
                "government_id": image,
            },
        )
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.parametrize(
        ("user_type", "status_code"),
        [("admin", status.HTTP_200_OK), ("user", status.HTTP_403_FORBIDDEN)],
    )
    def test_appointment_update_url(
        self,
        api_client: Client,
        user_type: str,
        admin_user: User,
        user: User,
        status_code: int,
        appointment: Appointment,
    ) -> None:
        """Test the appointment update url.

        Scenario:
            - As a user, I should not be able to update other user's appointment.
            - As an admin, I should be able to update every appointment.
        Args:
            api_client (Client): The api client sending the put request.
            appointment (Appointment): The appointment to be updated.
        """
        user_ = admin_user if user_type == "admin" else user
        api_client.force_login(user_)

        response = api_client.put(
            reverse("api:appointment-detail", kwargs={"pk": appointment.id}),
            {
                "recipient_name": appointment.recipient_name,
                "purpose": appointment.purpose + " Updated",
                "start_appointment": appointment.start_appointment,
                "document": appointment.document,
                "government_id": appointment.government_id,
            },
        )

        if user_type == "admin":
            assert response.data["purpose"] == appointment.purpose + " Updated"

        assert response.status_code == status_code

    @pytest.mark.parametrize(
        ("user_type", "status_code"),
        [("admin", status.HTTP_200_OK), ("user", status.HTTP_403_FORBIDDEN)],
    )
    def test_appointment_partial_update_url(
        self,
        api_client: Client,
        user_type: str,
        admin_user: User,
        user: User,
        status_code: int,
        appointment: Appointment,
    ) -> None:
        """Test the appointment partial update url.

        Scenario:
            - As a user, I should not be able to update other user's appointment.
            - As an admin, I should be able to update every appointment.
        Args:
            api_client (Client): The api client sending the patch request.
            appointment (Appointment): The appointment to be updated.
        """
        user_ = admin_user if user_type == "admin" else user
        api_client.force_login(user_)

        response = api_client.patch(
            reverse("api:appointment-detail", kwargs={"pk": appointment.id}),
            {
                "purpose": appointment.purpose + " Updated",
            },
        )

        if user_type == "admin":
            assert response.data["purpose"] == appointment.purpose + " Updated"

        assert response.status_code == status_code

    @pytest.mark.parametrize(
        ("user_type", "status_code"),
        [("admin", status.HTTP_204_NO_CONTENT), ("user", status.HTTP_403_FORBIDDEN)],
    )
    def test_appointment_delete_url(
        self,
        api_client: Client,
        user_type: str,
        admin_user: User,
        user: User,
        status_code: int,
        appointment: Appointment,
    ) -> None:
        """Test the appointment delete url.

        Scenario:
            - As a user, I should not be able to delete other user's appointment.
            - As an admin, I should be able to delete every appointment.
        Args:
            api_client (Client): The api client sending the delete request.
            appointment (Appointment): The appointment to be deleted.
        """
        user_ = admin_user if user_type == "admin" else user
        api_client.force_login(user_)

        response = api_client.delete(
            reverse("api:appointment-detail", kwargs={"pk": appointment.id})
        )

        assert response.status_code == status_code

    @staticmethod
    def test_appointment_me(api_client: Client, user: User) -> None:
        """Test the appointment me url.

        Scenario:
            - As a user, I should be able to get my appointments.
        Args:
            api_client (Client): The api client sending the get request.
            user_type (User): The user requesting the appointments.
        """
        api_client.force_login(user)

        for _ in range(2):
            Appointment.objects.create(
                recipient_name=f"{user.profile.first_name} {user.profile.last_name}",
                purpose="Test Appointment",
                start_appointment=datetime.now(tz=ZoneInfo("Asia/Manila")),
                document="IND",
                user=user,
            )

        response = api_client.get(reverse("api:appointment-me"))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2


class TestStatusViewSetUrls:
    """Test the StatusViewSet urls."""

    @staticmethod
    def test_status_retrieve_url(
        admin_api_client: Client, appointment: Appointment
    ) -> None:
        """Test the status retrieve url.

        Scenario:
            - As an admin, I should be able to access the status retrieve url.
        Args:
            admin_api_client (Client): The api client.
        """
        response = admin_api_client.get(
            reverse("api:appointment-detail", kwargs={"pk": appointment.id})
        )

        assert response.status_code == status.HTTP_200_OK

    @staticmethod
    def test_status_partial_update_url(
        admin_user: User, admin_api_client: Client
    ) -> None:
        """Test the status partial update url.

        Scenario:
            - As an admin, I should be able to access the status partial update url.
        Args:
            admin_api_client (Client): The admin api client.
        """
        a1 = Appointment.objects.create(
            recipient_name=f"{admin_user.profile.first_name} {admin_user.profile.last_name}",
            purpose="Test Appointment",
            start_appointment=datetime.now(tz=ZoneInfo("Asia/Manila")),
            document="IND",
            user=admin_user,
        )
        response = admin_api_client.patch(
            reverse("api:status-detail", kwargs={"pk": a1.id}),
            {"status": "APP"},
        )

        assert response.data["status"] == "Approved"
        assert response.status_code == status.HTTP_200_OK

    @staticmethod
    def test_status_update_url(admin_user: User, admin_api_client: Client) -> None:
        """Test the status update url.

        Scenario:
            - As an admin, I should be able to access the status update url.
        Args:
            admin_api_client (Client): The admin api client.
        """
        a1 = Appointment.objects.create(
            recipient_name=f"{admin_user.profile.first_name} {admin_user.profile.last_name}",
            purpose="Test Appointment",
            start_appointment=datetime.now(tz=ZoneInfo("Asia/Manila")),
            document="IND",
            user=admin_user,
        )
        response = admin_api_client.put(
            reverse("api:status-detail", kwargs={"pk": a1.id}),
            {"status": "CAN"},
        )

        assert response.data["status"] == "Cancelled"
        assert response.status_code == status.HTTP_200_OK
