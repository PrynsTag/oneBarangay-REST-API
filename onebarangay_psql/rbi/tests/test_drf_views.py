"""Create your rbi drf viewsets test here."""
import pytest
from django.test import RequestFactory
from django.urls import reverse
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request

from onebarangay_psql.rbi.models import FamilyMember, HouseRecord
from onebarangay_psql.rbi.serializers import (
    FamilyMemberSerializer,
    HouseRecordSerializer,
)
from onebarangay_psql.rbi.viewset import FamilyMemberViewSet, HouseRecordViewSet
from onebarangay_psql.users.models import User

pytestmark = pytest.mark.django_db


class TestHouseRecordViewSet:
    """Test HouseRecordViewSet."""

    @staticmethod
    def test_get_queryset(
        admin_user: User, house_record: HouseRecord, rf: RequestFactory
    ):
        """Test get_queryset returns a house record queryset.

        Scenario:
            - The get_queryset method should return a queryset of created house records.
        Args:
            admin_user (User): The admin user making the get request.
            house_record (HouseRecord): The house record to be returned.
            rf (RequestFactory): The request factory mocking the get request.
        """
        viewset = HouseRecordViewSet()

        request = rf.get(reverse("api:house-list"))
        request.user = admin_user

        viewset.request = Request(request)

        assert house_record in viewset.get_queryset()

    @staticmethod
    def test_get_serializer(admin_user: User, rf: RequestFactory):
        """Test get_serializer returns a HouseRecordSerializer.

        Scenario:
            - The get_serializer method should return an instance of HouseRecordSerializer.
        Args:
            admin_user (User): The admin user making the get request.
            rf (RequestFactory): The request factory mocking the get request.
        """
        viewset = HouseRecordViewSet()

        request = rf.get(reverse("api:house-list"))
        request.user = admin_user

        viewset.request = Request(request)
        viewset.format_kwarg = None

        assert isinstance(viewset.get_serializer(), HouseRecordSerializer)

    @staticmethod
    def test_get_permission(admin_user: User, rf: RequestFactory):
        """Test get_permission returns IsAdminUser.

        Scenario:
            - The get_permission method should return an instance of IsAdminUser.
        Args:
            admin_user (User): The admin user making the get request.
            rf (RequestFactory): The request factory mocking the get request.
        """
        viewset = HouseRecordViewSet()

        request = rf.get(reverse("api:house-list"))
        request.user = admin_user

        viewset.request = Request(request)
        viewset.format_kwarg = None

        assert isinstance(viewset.get_permissions()[0], IsAdminUser)


class TestFamilyMemberViewSet:
    """Test FamilyMemberViewSet."""

    @staticmethod
    def test_get_queryset(
        admin_user: User, family_member: FamilyMember, rf: RequestFactory
    ):
        """Test get_queryset returns a family member queryset.

        Scenario:
            - The get_queryset method should return a queryset of created family members.
        Args:
            admin_user (User): The admin user making the get request.
            family_member (FamilyMember): The family member to be returned.
            rf (RequestFactory): The request factory to mock get request.
        """
        viewset = FamilyMemberViewSet()

        request = rf.get(reverse("api:family-list"))
        request.user = admin_user

        viewset.request = Request(request)

        assert family_member in viewset.get_queryset()

    @staticmethod
    def test_get_serializer(admin_user: User, rf: RequestFactory):
        """Test get_serializer returns an instance of FamilyMemberSerializer.

        Scenario:
            - The get_serializer method should return an instance of FamilyMemberSerializer.
        Args:
            admin_user (User): The admin user making the get request.
            rf (RequestFactory): The request factory to mock get request.
        """
        viewset = FamilyMemberViewSet()

        request = rf.get(reverse("api:family-list"))
        request.user = admin_user

        viewset.request = Request(request)
        viewset.format_kwarg = None

        assert isinstance(viewset.get_serializer(), FamilyMemberSerializer)

    @staticmethod
    def test_get_permission(admin_user: User, rf: RequestFactory):
        """Test get_permission returns an instance of IsAdminUser.

        Scenario:
            - The get_permission method should return an instance of IsAdminUser.
        Args:
            admin_user (User): The admin user making the get request.
            rf (RequestFactory): The request factory to mock get request.
        """
        viewset = FamilyMemberViewSet()

        request = rf.get(reverse("api:family-list"))
        request.user = admin_user

        viewset.request = Request(request)
        viewset.format_kwarg = None

        assert isinstance(viewset.get_permissions()[0], IsAdminUser)
