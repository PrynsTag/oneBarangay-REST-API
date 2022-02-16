"""Create your appointment views here."""
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from onebarangay_psql.appointment.models import Appointment
from onebarangay_psql.appointment.permissions import IsCreatorOrAdmin
from onebarangay_psql.appointment.serializer import (
    AppointmentSerializer,
    StatusSerializer,
)


class AppointmentViewSet(viewsets.ModelViewSet):
    """Appointment viewset."""

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_permissions(self):
        """Return the appropriate permissions that each action requires."""
        if self.action in ["retrieve", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsCreatorOrAdmin]
        elif self.action == "list":
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        """Set the creator of the appointment."""
        serializer.save(user=self.request.user)

    @action(detail=False)
    def me(self, request):
        """Return the appointments of the current user."""
        appointments = Appointment.objects.filter(user=request.user)
        serializer = self.get_serializer(appointments, many=True)
        return Response(serializer.data)


class StatusUpdateViewSet(
    mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """Update the status of an appointment."""

    queryset = Appointment.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        """Get the appointment object."""
        return Appointment.objects.get(id=self.kwargs["pk"])

    def perform_update(self, serializer):
        """Set the status of the appointment."""
        serializer.save(status=self.request.data["status"])
