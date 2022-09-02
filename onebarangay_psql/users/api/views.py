"""Create your user API views here."""
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from push_notifications.api.rest_framework import (
    GCMDeviceAuthorizedViewSet,
    GCMDeviceSerializer,
)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import (
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from onebarangay_psql.users.api.serializers import (
    ProfileImageSerializer,
    ProfileSerializer,
    UserSerializer,
)
from onebarangay_psql.users.models import Profile
from onebarangay_psql.users.permissions import IsOwnProfile

User = get_user_model()


class UserViewSet(
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """Retrieve and update user profile."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"
    filterset_fields = ["username"]
    search_fields = ["username"]

    def get_permissions(self):
        """Return the appropriate permissions that each action requires."""
        if self.action in ["retrieve", "update", "partial_update", "destroy", "me"]:
            self.permission_classes = [IsOwnProfile]
        else:
            # Only admin can list all users
            self.permission_classes = [IsAdminUser]
        return [permission() for permission in self.permission_classes]

    def get_object(self):
        """Get User object.

        Get user data if user is admin or user is requesting their own data.

        Returns:
            (User): User object.
        """
        if self.request.user.is_superuser:
            return get_object_or_404(self.queryset, username=self.kwargs["username"])
        if self.request.user.username != self.kwargs["username"]:
            raise PermissionDenied

        return get_object_or_404(self.queryset, username=self.kwargs["username"])

    @action(detail=False)
    def me(self, request) -> Response:
        """Get the currently authenticated user.

        Args:
            request (FixtureRequest): request object.

        Returns:
            (Response): response object.
        """
        if str(request.user) == "AnonymousUser":
            raise PermissionDenied
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProfileViewSet(
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """Retrieve or Update user profile."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "username"

    def get_permissions(self):
        """Return the appropriate permissions that each action requires."""
        if self.action in ["retrieve", "update", "partial_update", "destroy", "me"]:
            self.permission_classes = [IsOwnProfile]
        else:
            # Only admin can list all profiles
            self.permission_classes = [IsAdminUser]
        return [permission() for permission in self.permission_classes]

    def get_object(self):
        """Return Profile object for ProfileViewSet view.

        Return a Profile object if user is admin or the user is
        requesting its own data.

        Returns:
            (Profile): Profile object.
        """
        if self.request.user.is_superuser:
            return get_object_or_404(
                self.queryset, user__username=self.kwargs["username"]
            )
        if self.request.user.username != self.kwargs["username"]:
            raise PermissionDenied

        return get_object_or_404(
            self.queryset, user__username=self.kwargs["username"]
        )

    @action(detail=False)
    def me(self, request) -> Response:
        """Get the currently authenticated user.

        Args:
            request (FixtureRequest): FixtureRequest object.

        Returns:
            (Response): Response object.
        """
        if str(self.request.user) == "AnonymousUser":
            raise PermissionDenied
        data = self.queryset.get(user__username=self.request.user.username)
        serializer = ProfileSerializer(data, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfilePhotoViewSet(UpdateModelMixin, GenericViewSet):
    """Update user profile photo."""

    queryset = Profile.objects.all()
    serializer_class = ProfileImageSerializer
    lookup_field = "user__username"

    def patch(self, request):
        """Change user profile photo."""
        if str(self.request.user) == "AnonymousUser":
            raise PermissionDenied
        image = request.data["profile_image"]
        data = self.queryset.get(user__username=self.request.user.username)
        data.profile_image = image
        serializer = ProfileImageSerializer(
            data, context={"request": request}, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GCMAuthorizedFilterSet(GCMDeviceAuthorizedViewSet):
    """Filter GCMDeviceAuthorizedViewSet by authorized devices."""

    filterset_fields = ["id"]

    @action(detail=False, methods=["get"])
    def me(self, request):
        """Get the GCM data of the currently authenticated user.

        Args:
            request (FixtureRequest): FixtureRequest object.

        Returns:
            (Response): Response object.
        """
        if str(self.request.user) == "AnonymousUser":
            raise PermissionDenied
        data = self.queryset.get(user__username=self.request.user.username)
        serializer = GCMDeviceSerializer(data, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
