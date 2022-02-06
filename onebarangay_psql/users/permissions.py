"""Create your custom permissions for user's app."""
from django.views import View
from rest_framework import permissions
from rest_framework.request import Request

from onebarangay_psql.users.models import Profile


class IsOwnProfile(permissions.BasePermission):
    """Allow access only to the user's profile."""

    def has_object_permission(self, request: Request, view: View, obj: Profile) -> bool:
        """Check if the user is trying to access their own profile or user data.

        Args:
            request (Request): The request object.
            view (View): The view object.
            obj (Profile): The user object.

        Returns:
            bool: True if the user is trying to access their own profile.
        """
        if view.__class__ == Profile:
            return obj.user == request.user
        return obj == request.user
