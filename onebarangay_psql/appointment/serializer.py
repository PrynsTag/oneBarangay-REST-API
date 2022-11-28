"""Create your appointment serializer here."""
from rest_framework_json_api import serializers
from rest_framework_json_api.relations import HyperlinkedRelatedField

from onebarangay_psql.appointment.models import Appointment
from onebarangay_psql.utils.choice_field import ChoicesField


class AppointmentSerializer(serializers.ModelSerializer):
    """Appointment Serializer."""

    document = ChoicesField(choices=Appointment.Document.choices)
    status = ChoicesField(choices=Appointment.Status.choices)
    user: HyperlinkedRelatedField = serializers.HyperlinkedRelatedField(
        view_name="api:user-detail", lookup_field="username", read_only=True
    )
    username = serializers.ReadOnlyField(source="user.username")
    email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        """Meta class."""

        model = Appointment
        ordering = ["created_at"]
        fields = "__all__"
        read_only_fields = ["end_appointment"]


class StatusSerializer(serializers.ModelSerializer):
    """Status Serializer."""

    status = ChoicesField(choices=Appointment.Status.choices)

    class Meta:
        """Meta class."""

        model = Appointment
        fields = ["status"]
