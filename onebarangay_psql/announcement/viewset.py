"""Create your announcement views here."""
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

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
