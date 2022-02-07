"""Create your user API views here."""
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from onebarangay_psql.users.api.serializers import UserProfileSerializer, UserSerializer
from onebarangay_psql.users.models import Profile
from onebarangay_psql.users.permissions import IsOwnProfile

User = get_user_model()


class UserViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """Retrieve and update user profile."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"
    permission_classes = [IsAuthenticated & (IsOwnProfile | IsAdminUser)]

    def get_queryset(self, *args, **kwargs):
        """Get the User queryset for the currently authenticated user.

        Args:
            *args (list): list of arguments.
            **kwargs (dict): dictionary of keyword arguments.

        Returns:
            (QuerySet) queryset.
        """
        user = self.request.user
        assert isinstance(user.id, int)
        return self.queryset.filter(username=user.username)

    def get_object(self):
        """Get User object.

        Get user data if user is admin or user is requesting their own data.

        Returns:
            (User): User object.
        """
        if self.request.user.is_superuser:
            return get_object_or_404(self.queryset, username=self.kwargs["username"])
        else:
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
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class UserListViewSet(ListModelMixin, GenericViewSet):
    """List all users."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated & IsAdminUser]
    lookup_field = "username"


class UserProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """Retrieve or Update user profile."""

    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "username"
    permission_classes = [IsAuthenticated & (IsOwnProfile | IsAdminUser)]

    def get_queryset(self):
        """Get for the requesting user.

        Returns:
            (Profile): Profile queryset.
        """
        user = self.request.user
        assert isinstance(user.id, int)
        return self.queryset.filter(user__username=user.username).first()

    def get_object(self):
        """Return Profile object for UserProfileViewSet view.

        Return a Profile object if user is admin or the user is
        requesting its own data.

        Returns:
            (Profile): Profile object.
        """
        if self.request.user.is_superuser:
            return get_object_or_404(
                self.queryset, user__username=self.kwargs["username"]
            )
        else:
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
        data = self.queryset.get(user__username=self.request.user.username)
        serializer = UserProfileSerializer(data, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileListViewSet(ListModelMixin, GenericViewSet):
    """List all user profiles."""

    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "username"
    permission_classes = [IsAuthenticated & IsAdminUser]
