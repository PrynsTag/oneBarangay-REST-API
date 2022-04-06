"""Create your announcement views here."""
from django.utils.html import strip_tags
from push_notifications.models import GCMDevice
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from onebarangay_psql.announcement.models import Announcement
from onebarangay_psql.announcement.serializer import AnnouncementSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    """Announcement ViewSet."""

    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = "slug"

    def get_permissions(self):
        """Return appropriate permissions per action."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        """Save announcement with currently logged-in user.

        Args:
            serializer (AnnouncementSerializer): The Announcement serializer data to save.
        """
        serializer.save(author=self.request.user)
        data = serializer.data
        GCMDevice.objects.all().send_message(
            message={"title": data["title"], "body": strip_tags(data["content"])}
        )

    @action(detail=False)
    def me(self, request) -> Response:
        """Get the currently authenticated user.

        Args:
            request (FixtureRequest): request object.

        Returns:
            (Response): response object.
        """
        queryset = self.queryset.filter(author=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
