"""Create your statistics drf viewsets test here."""
import pytest
from django.test import RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from onebarangay_psql.statistics import serializers, viewset
from onebarangay_psql.users.models import User


class TestStatisticsViewSet:
    """Test StatisticsViewSet."""

    @pytest.mark.parametrize(
        ("app_url", "app_viewset", "serializer"),
        [
            (
                "api:mv-signup-list",
                viewset.UserSignUpMaterializedViewSet,
                serializers.UserSignUpMaterializedViewSerializer,
            ),
            (
                "api:mv-total-list",
                viewset.TotalMaterializedViewSet,
                serializers.TotalMaterializedViewSerializer,
            ),
            (
                "api:mv-appointment-list",
                viewset.AppointmentMaterializedViewSet,
                serializers.AppointmentMaterializedViewSerializer,
            ),
            (
                "api:mv-signin-list",
                viewset.UserLogInMaterializedViewSet,
                serializers.UserLogInMaterializedViewSerializer,
            ),
            (
                "api:mv-age-group-list",
                viewset.AgeGroupMaterializedViewSet,
                serializers.AgeGroupMaterializedViewSerializer,
            ),
            (
                "api:mv-citizenship-list",
                viewset.CitizenshipMaterializedViewSet,
                serializers.CitizenshipMaterializedViewSerializer,
            ),
            (
                "api:mv-civil-status-list",
                viewset.CivilStatusMaterializedViewSet,
                serializers.CivilStatusMaterializedViewSerializer,
            ),
            (
                "api:mv-average-list",
                viewset.AverageMaterializedViewSet,
                serializers.AverageMaterializedViewSerializer,
            ),
            (
                "api:mv-social-class-list",
                viewset.SocialClassMaterializedViewSet,
                serializers.SocialClassMaterializedViewSerializer,
            ),
            (
                "api:mv-refresh-list",
                viewset.RefreshMaterialViewSet,
                serializers.RefreshMaterializedViewSerializer,
            ),
        ],
    )
    def test_get_serializer(
        self,
        admin_user: User,
        app_url: str,
        app_viewset,
        serializer,
        rf: RequestFactory,
    ):
        """Test get_serializer returns a HouseRecordSerializer.

        Scenario:
            - The get_serializer method should return an instance of HouseRecordSerializer.
        Args:
            admin_user (User): The admin user making the get request.
            rf (RequestFactory): The request factory mocking the get request.
        """
        viewsets = app_viewset

        request = rf.get(reverse(app_url))
        request.user = admin_user

        viewsets.request = Request(request)
        viewsets.format_kwarg = None

        assert viewsets.serializer_class == serializer

    @pytest.mark.parametrize(
        ("app_url", "app_viewset"),
        [
            (
                "api:mv-signup-list",
                viewset.UserSignUpMaterializedViewSet,
            ),
            (
                "api:mv-total-list",
                viewset.TotalMaterializedViewSet,
            ),
            (
                "api:mv-appointment-list",
                viewset.AppointmentMaterializedViewSet,
            ),
            (
                "api:mv-signin-list",
                viewset.UserLogInMaterializedViewSet,
            ),
            (
                "api:mv-age-group-list",
                viewset.AgeGroupMaterializedViewSet,
            ),
            (
                "api:mv-citizenship-list",
                viewset.CitizenshipMaterializedViewSet,
            ),
            (
                "api:mv-civil-status-list",
                viewset.CivilStatusMaterializedViewSet,
            ),
            (
                "api:mv-average-list",
                viewset.AverageMaterializedViewSet,
            ),
            (
                "api:mv-social-class-list",
                viewset.SocialClassMaterializedViewSet,
            ),
            (
                "api:mv-refresh-list",
                viewset.RefreshMaterialViewSet,
            ),
        ],
    )
    def test_get_permission(
        self, admin_user: User, app_url: str, app_viewset, rf: RequestFactory
    ):
        """Test get_permission returns IsAdminUser.

        Scenario:
            - The get_permission method should return an instance of IsAdminUser.
        Args:
            admin_user (User): The admin user making the get request.
            rf (RequestFactory): The request factory mocking the get request.
        """
        viewsets = app_viewset

        request = rf.get(reverse(app_url))
        request.user = admin_user

        viewsets.request = Request(request)
        viewsets.format_kwarg = None

        assert viewsets.permission_classes[0] == IsAuthenticated


def test_refresh_materialized_viewset_create(admin_user: User, rf: RequestFactory):
    """Test RefreshMaterializedViewset create method.

    Scenario:
        - The create method should return a response with status code 201.
    Args:
        admin_user (User): The admin user making the post request.
        rf (RequestFactory): The request factory mocking the get request.
    """
    viewsets = viewset.RefreshMaterialViewSet()

    request = Request(rf.post(reverse("api:mv-refresh-list")))
    request.user = admin_user

    viewsets.request = request
    viewsets.format_kwarg = None

    response = viewsets.create(request)

    assert response.status_code == status.HTTP_201_CREATED
