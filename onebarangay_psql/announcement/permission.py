"""Create your announcement permissions here."""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it."""

    def has_object_permission(self, request, view, obj):
        """Permission to only allow owners of an object to edit it.

        Args:
            request (Request): The request object.
            view (View): The view object.
            obj (Object): The object the user is trying to edit.

        Returns:
            bool: True if the user is the owner of the object. False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
