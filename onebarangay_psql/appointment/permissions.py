"""Create your appointment permissions here."""
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

from onebarangay_psql.appointment.models import Appointment


class IsCreatorOrAdmin(permissions.BasePermission):
    """Check if the user is the creator of the appointment."""

    def has_permission(self, request: Request, view: APIView) -> bool:
        """Return `True` if user is authenticated, `False` otherwise.

        Args:
            request (Request): Django request object.
            view (APIView): Django view object.

        Returns:
            bool: `True` if user is authenticated, `False` otherwise.
        """
        return request.user.is_authenticated

    def has_object_permission(
        self, request: Request, view: APIView, obj: Appointment
    ) -> bool:
        """Return `True` if user is the creator, `False` otherwise.

        Args:
            request (Request): Django request object.
            view (APIView): Django view object.
            obj (Appointment): Django model object.

        Returns:
            bool: `True` if user is the creator, `False` otherwise.
        """
        return (obj.user == request.user) or request.user.is_staff
