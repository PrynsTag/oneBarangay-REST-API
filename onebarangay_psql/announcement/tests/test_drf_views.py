"""Create your announcement drf viewset tests here."""
import pytest
from _pytest.fixtures import FixtureRequest
from django.test import RequestFactory
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated

from onebarangay_psql.announcement.models import Announcement
from onebarangay_psql.announcement.serializer import AnnouncementSerializer
from onebarangay_psql.announcement.viewset import AnnouncementViewSet
from onebarangay_psql.users.models import User

pytestmark = pytest.mark.django_db


# mypy: ignore-errors
class TestAnnouncementViewSet:
    """Test DRF AnnouncementViewSet View."""

    def test_get_queryset(
        self, user: User, announcement: Announcement, rf: RequestFactory
    ) -> None:
        """Test 'get_queryset' returns the announcement queryset.

        Args:
            user (User): The logged-in user.
            announcement (Announcement): The announcement queryset to check.
            rf (RequestFactory): The request factory.
        """
        view = AnnouncementViewSet()

        request = rf.get("/fake-url/")
        request.user = user
        request.announcement = announcement

        view.request = request

        assert announcement in view.get_queryset()

    # pylint: disable=redefined-outer-name
    @pytest.mark.parametrize(
        ("user_type", "permission"), [("admin", IsAdminUser), ("user", IsAuthenticated)]
    )
    def test_get_permission(
        self,
        announcement: Announcement,
        rf: RequestFactory,
        user_type: User,
        permission: BasePermission,
    ) -> None:
        """Test 'get_permission' returns the correct permission.

        Args:
            announcement (Announcement): The required object of AnnouncementViewSet.
            rf (RequestFactory): The request factory.
            user_type (User): The logged-in user.
            permission (BasePermission): The permission to check.
        """
        view = AnnouncementViewSet()

        request = rf.get("/fake-url/")
        request.user = user_type
        request.announcement = announcement

        view.request = request
        view.action = "retrieve" if user_type == "user" else "create"

        permission_class: BasePermission = view.get_permissions()[0]

        assert isinstance(permission_class, permission)

    def test_perform_create(self, user: User, rf: RequestFactory) -> None:
        """Test 'perform_create' creates the announcement.

        Args:
            user (User): The logged-in user.
            rf (RequestFactory): The request factory.
        """
        view = AnnouncementViewSet()
        serializer = AnnouncementSerializer()
        announcement_data = {"title": "Test", "content": "Test", "tags": '["Test"]'}

        request = rf.post("/fake-url/")
        request.user = user
        request.data = announcement_data

        view.request = request
        view.format_kwarg = None
        view.serializer = serializer

        response = view.create(request)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["title"] == "Test"
        assert response.data["content"] == "Test"


@pytest.fixture()
def user_type(request: FixtureRequest, user: User, admin_user: User):
    """Return different user type.

    Args:
        request (pytest.fixture): pytest fixture.
        user (User): User object.
        admin_user (User): Admin user object.

    Returns:
        User: User object.
    """
    if request.param == "user":
        return user
    else:
        return admin_user
