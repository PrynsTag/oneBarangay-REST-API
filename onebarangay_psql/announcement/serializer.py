"""Create your announcement serializer here."""
from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from onebarangay_psql.announcement.models import Announcement


class AnnouncementSerializer(TaggitSerializer, serializers.ModelSerializer):
    """Serializer for Announcement model."""

    tags = TagListSerializerField()
    author = serializers.HyperlinkedIdentityField(
        view_name="api:profile-detail", lookup_field="username"
    )
    url = serializers.HyperlinkedIdentityField(
        view_name="api:announcement-detail", lookup_field="slug"
    )

    class Meta:
        """Meta class for AnnouncementSerializer."""

        model = Announcement
        fields = "__all__"
        ordering = ["-created_at"]
        read_only_fields = ["slug", "username"]
