"""Create your user and profile serializers here."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField

from onebarangay_psql.users.models import Profile
from onebarangay_psql.utils.choice_field import ChoicesField


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user objects."""

    id = serializers.CharField(source="username", read_only=True)

    class Meta:
        """Meta class for user serializer."""

        model = User
        fields = [
            "id",
            "last_login",
            "is_superuser",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
            "url",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile objects."""

    user: HyperlinkedRelatedField = serializers.HyperlinkedRelatedField(
        view_name="api:profile-detail", lookup_field="username", read_only=True
    )
    email = serializers.CharField(source="user.email", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    gender = ChoicesField(choices=Profile.Gender.choices)
    civil_status = ChoicesField(choices=Profile.CivilStatus.choices)

    class Meta:
        """Meta class for user profile serializer."""

        model = Profile
        fields = "__all__"

        extra_kwargs = {
            "url": {"view_name": "api:profile-detail", "lookup_field": "username"}
        }


class ProfileImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading profile images."""

    class Meta:
        """Meta class for profile image serializer."""

        model = Profile
        fields = ("profile_image",)
