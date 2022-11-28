"""Create your appointment drf viewset tests here."""
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAdminUser

from config.settings.base import APPS_DIR
from onebarangay_psql.appointment.models import Appointment
from onebarangay_psql.appointment.permissions import IsCreatorOrAdmin
from onebarangay_psql.appointment.serializer import (
    AppointmentSerializer,
    StatusSerializer,
)
from onebarangay_psql.appointment.viewset import AppointmentViewSet, StatusUpdateViewSet
from onebarangay_psql.users.models import User


pytestmark = pytest.mark.django_db


# mypy: ignore-errors
class TestAppointmentViewSet:
    """Test DRF AppointmentViewSet View."""

    @staticmethod
    def test_get_queryset(
        user: User, appointment: Appointment, rf: RequestFactory
    ) -> None:
        """Test 'get_queryset' returns the appointment queryset.

        Args:
            user (User): The logged-in user sending the get request.
            appointment (Appointment): The appointment queryset to get back from the view.
            rf (RequestFactory): The request factory to fake the request.
        """
        view = AppointmentViewSet()

        request = rf.get("/fake-url/")
        request.user = user
        request.appointment = appointment

        view.request = request

        assert appointment in view.get_queryset()

    # pylint: disable=redefined-outer-name
    @pytest.mark.parametrize(
        ("user_type", "permission"),
        [("admin", IsAdminUser), ("user", IsCreatorOrAdmin)],
    )
    def test_get_permission(
        self,
        appointment: Appointment,
        rf: RequestFactory,
        user_type: User,
        permission: BasePermission,
    ) -> None:
        """Test 'get_permission' returns the correct permission.

        Args:
            appointment (Appointment): The required object of AppointmentViewSet.
            rf (RequestFactory): The request factory to fake the request.
            user_type (User): The logged-in user sending the get request.
            permission (BasePermission): The permission to check.
        """
        view = AppointmentViewSet()

        request = rf.get("/fake-url/")
        request.user = user_type
        request.appointment = appointment

        view.request = request
        view.action = "retrieve" if user_type == "user" else "list"

        permission_class: BasePermission = view.get_permissions()[0]

        assert isinstance(permission_class, permission)

    @staticmethod
    def test_perform_create(user: User, rf: RequestFactory) -> None:
        """Test 'perform_create' creates the appointment.

        Args:
            user (User): The logged-in user sending the post request.
            rf (RequestFactory): The request factory to fake the request.
        """
        with open(APPS_DIR / "media/appointment/government_id/default.png", "rb") as f:
            image = SimpleUploadedFile(f.name, f.read(), content_type="image/jpeg")

        view = AppointmentViewSet()
        serializer = AppointmentSerializer()
        appointment_data = {
            "recipient_name": "Prince Velasco",
            "purpose": "Test Appointment",
            "start_appointment": datetime.now(tz=ZoneInfo("Asia/Manila")),
            "document": "IND",
            "government_id": image,
            "status": "PEN",
        }

        request = rf.post("/fake-url/")
        request.user = user
        request.data = appointment_data
        request.query_params = {}

        view.request = request
        view.format_kwarg = None
        view.serializer = serializer

        response = view.create(request)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["recipient_name"] == "Prince Velasco"
        assert response.data["purpose"] == "Test Appointment"

    @staticmethod
    def test_appointment_me(admin_user: User, rf: RequestFactory) -> None:
        """Test 'appointment_me' returns the logged-in user's appointment.

        Args:
            admin_user (User): The logged-in user sending the get request.
            rf (RequestFactory): The request factory to fake the request.
        """
        view = AppointmentViewSet()

        request = rf.get("/fake-url/")
        request.user = admin_user
        request.query_params = {}

        view.request = request
        view.format_kwarg = None

        response = view.me(request)

        assert response.status_code == status.HTTP_200_OK


class TestStatusUpdateViewSet:
    """Test the StatusUpdateViewSet."""

    @staticmethod
    def test_get_object(appointment: Appointment, rf: RequestFactory) -> None:
        """Test 'get_object' returns the appointment.

        Args:
            appointment (Appointment): The required object of AppointmentViewSet.
            rf (RequestFactory): The request factory to fake the request.
        """
        view = StatusUpdateViewSet()

        request = rf.get("/fake-url/")
        request.appointment = appointment

        view.request = request
        view.kwargs = {"pk": appointment.pk}

        assert view.get_object() == appointment

    @staticmethod
    def test_perform_create(appointment: Appointment, rf: RequestFactory) -> None:
        """Test 'perform_create' creates the status update.

        Args:
            appointment (Appointment): The appointment queryset to get back from the view.
            rf (RequestFactory): The request factory.
        """
        view = StatusUpdateViewSet()
        serializer = StatusSerializer()
        status_update_data = {"status": "CAN"}

        request = rf.post("/fake-url/")
        request.appointment = appointment
        request.data = status_update_data
        request.query_params = {}

        view.request = request
        view.format_kwarg = None
        view.serializer = serializer
        view.kwargs = {"pk": appointment.pk}

        response = view.update(request)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["status"] == "Cancelled"
