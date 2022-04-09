"""Create your custom choice field here."""
from rest_framework import serializers


class ChoicesField(serializers.ChoiceField):
    """Custom ChoiceField to handle human-readable choices."""

    def to_representation(self, value):
        """Return the human-readable choice."""
        return self.choices.get(value, None)
