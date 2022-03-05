"""Create your statistics serializers here."""
from rest_framework import serializers

from onebarangay_psql.statistics import models


class TotalMaterializedViewSerializer(serializers.ModelSerializer):
    """Total Materialized View Serializer."""

    class Meta:
        """Meta class for TotalMaterializedViewSerializer."""

        model = models.TotalMaterializedView
        fields = "__all__"


class UserSignUpMaterializedViewSerializer(serializers.ModelSerializer):
    """User Signup Materialized View Serializer."""

    class Meta:
        """Meta class for UserSignupMaterializedViewSerializer."""

        model = models.UserSignUpMaterializedView
        fields = "__all__"


class UserSignUpMonthlyMaterializedViewSerializer(serializers.ModelSerializer):
    """User Signup Monthly Materialized View Serializer."""

    class Meta:
        """Meta class for UserSignupMonthlyMaterializedViewSerializer."""

        model = models.UserSignUpMonthlyMaterializedView
        fields = "__all__"


class UserLoginMonthlyMaterializedViewSerializer(serializers.ModelSerializer):
    """User Login Monthly Materialized View Serializer."""

    class Meta:
        """Meta class for UserLoginMonthlyMaterializedViewSerializer."""

        model = models.UserLoginMonthlyMaterializedView
        fields = "__all__"


class AppointmentMaterializedViewSerializer(serializers.ModelSerializer):
    """Appointment Materialized View Serializer."""

    class Meta:
        """Meta class for AppointmentMaterializedViewSerializer."""

        model = models.AppointmentMaterializedView
        fields = "__all__"


class UserLogInMaterializedViewSerializer(serializers.ModelSerializer):
    """User Login Materialized View Serializer."""

    class Meta:
        """Meta class for UserLogInMaterializedViewSerializer."""

        model = models.UserLogInMaterializedView
        fields = "__all__"


class AgeGroupMaterializedViewSerializer(serializers.ModelSerializer):
    """Age Group Materialized View Serializer."""

    class Meta:
        """Meta class for AgeGroupMaterializedViewSerializer."""

        model = models.AgeGroupMaterializedView
        fields = "__all__"


class CitizenshipMaterializedViewSerializer(serializers.ModelSerializer):
    """Citizenship Materialized View Serializer."""

    class Meta:
        """Meta class for CitizenshipMaterializedViewSerializer."""

        model = models.CitizenshipMaterializedView
        fields = "__all__"


class CivilStatusMaterializedViewSerializer(serializers.ModelSerializer):
    """Civil Status Materialized View Serializer."""

    class Meta:
        """Meta class for CivilStatusMaterializedViewSerializer."""

        model = models.CivilStatusMaterializedView
        fields = "__all__"


class AverageMaterializedViewSerializer(serializers.ModelSerializer):
    """Average Materialized View Serializer."""

    class Meta:
        """Meta class for AverageMaterializedViewSerializer."""

        model = models.AverageMaterializedView
        fields = "__all__"


class SocialClassMaterializedViewSerializer(serializers.ModelSerializer):
    """Social Class Materialized View Serializer."""

    class Meta:
        """Meta class for SocialClassMaterializedViewSerializer."""

        model = models.SocialClassMaterializedView
        fields = "__all__"


class RefreshMaterializedViewSerializer(serializers.ModelSerializer):
    """Refresh Materialized View Serializer."""

    class Meta:
        """Meta class for RefreshMaterializedViewSerializer."""

        model = models.RefreshMaterializedView
        fields = "__all__"
