"""Create your appointment serializer here."""
from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField

from onebarangay_psql.appointment.models import Appointment


class ChoicesField(serializers.ChoiceField):
    """Custom ChoiceField to handle human-readable choices."""

    def to_representation(self, value):
        """Return the human-readable choice."""
        return self.choices[value]


class AppointmentSerializer(serializers.ModelSerializer):
    """Appointment Serializer."""

    document = ChoicesField(choices=Appointment.Document.choices)
    status = ChoicesField(choices=Appointment.Status.choices, read_only=True)
    user: HyperlinkedRelatedField = serializers.HyperlinkedRelatedField(
        view_name="api:user-detail", lookup_field="username", read_only=True
    )
    status_url = serializers.HyperlinkedIdentityField(view_name="api:status-detail")
    url = serializers.HyperlinkedIdentityField(view_name="api:appointment-detail")
    username = serializers.ReadOnlyField(source="user.username")
    email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        """Meta class."""

        model = Appointment
        ordering = ["created_at"]
        fields = "__all__"
        read_only_fields = ["end_appointment", "url"]


class StatusSerializer(serializers.ModelSerializer):
    """Status Serializer."""

    status = ChoicesField(choices=Appointment.Status.choices)

    class Meta:
        """Meta class."""

        model = Appointment
        fields = ["status"]
