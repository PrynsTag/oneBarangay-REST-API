"""Create your statistics viewsets here."""
import datetime
import time
from typing import Any

from django.db import connection, transaction
from rest_framework import mixins, status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from onebarangay_psql.statistics import models, serializers


class TotalMaterializedViewSet(viewsets.ReadOnlyModelViewSet):
    """Display the total number of person per category."""

    queryset = models.TotalMaterializedView.objects.all()
    serializer_class = serializers.TotalMaterializedViewSerializer


class UserSignUpMaterializedViewSet(viewsets.ReadOnlyModelViewSet):
    """Display the total number of user sign-ups per month."""

    queryset = models.UserSignUpMaterializedView.objects.all()
    serializer_class = serializers.UserSignUpMaterializedViewSerializer


class AppointmentMaterializedViewSet(viewsets.ReadOnlyModelViewSet):
    """Display the total number of appointments per day."""

    queryset = models.AppointmentMaterializedView.objects.all()
    serializer_class = serializers.AppointmentMaterializedViewSerializer


class UserLogInMaterializedViewSet(viewsets.ReadOnlyModelViewSet):
    """Display the total number of user log-ins per day."""

    queryset = models.UserLogInMaterializedView.objects.all()
    serializer_class = serializers.UserLogInMaterializedViewSerializer


class AgeGroupMaterializedViewSet(viewsets.ReadOnlyModelViewSet):
    """Display the total number of person per age group."""

    queryset = models.AgeGroupMaterializedView.objects.all()
    serializer_class = serializers.AgeGroupMaterializedViewSerializer


class CitizenshipMaterializedViewSet(viewsets.ReadOnlyModelViewSet):
    """Display the total number of person per citizenship."""

    queryset = models.CitizenshipMaterializedView.objects.all()
    serializer_class = serializers.CitizenshipMaterializedViewSerializer


class CivilStatusMaterializedViewSet(viewsets.ReadOnlyModelViewSet):
    """Display the total number of person per civil status."""

    queryset = models.CivilStatusMaterializedView.objects.all()
    serializer_class = serializers.CivilStatusMaterializedViewSerializer


class AverageMaterializedViewSet(viewsets.ReadOnlyModelViewSet):
    """Display the averages per category."""

    queryset = models.AverageMaterializedView.objects.all()
    serializer_class = serializers.AverageMaterializedViewSerializer


class SocialClassMaterializedViewSet(viewsets.ReadOnlyModelViewSet):
    """Display the total number of person per social class."""

    queryset = models.SocialClassMaterializedView.objects.all()
    serializer_class = serializers.SocialClassMaterializedViewSerializer


class UserSignUpMonthlyMaterializedViewSet(viewsets.ReadOnlyModelViewSet):
    """Display the total number of user sign-ups per month."""

    queryset = models.UserSignUpMonthlyMaterializedView.objects.all()
    serializer_class = serializers.UserSignUpMonthlyMaterializedViewSerializer


class UserLoginMonthlyMaterializedViewSet(viewsets.ReadOnlyModelViewSet):
    """Display the total number of user log-ins per month."""

    queryset = models.UserLoginMonthlyMaterializedView.objects.all()
    serializer_class = serializers.UserLoginMonthlyMaterializedViewSerializer


class RefreshMaterialViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """Refreshes the materialized views in the database."""

    queryset = models.RefreshMaterializedView.objects.all()
    serializer_class = serializers.RefreshMaterializedViewSerializer

    @transaction.atomic
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Create a new refresh materialized view."""
        start_time = time.monotonic()
        with connection.cursor() as cursor:
            cursor.execute(
                """
            REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_total;
            REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_user_signup;
            REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_appointment;
            REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_user_login;
            REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_age_group;
            REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_citizenship;
            REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_civil_status;
            REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_average;
            REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_social_class;
            REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_user_signup_monthly;
            REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_user_login_monthly;
            """
            )
        end_time = time.monotonic()

        serializer = self.get_serializer(
            data={"duration": datetime.timedelta(seconds=end_time - start_time)}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
