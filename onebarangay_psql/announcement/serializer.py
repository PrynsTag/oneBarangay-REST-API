"""Create your announcement serializer here."""
from rest_framework_json_api import serializers
from rest_framework_json_api.relations import HyperlinkedRelatedField
from taggit.serializers import TaggitSerializer, TagListSerializerField

from onebarangay_psql.announcement.models import Announcement


class AnnouncementSerializer(TaggitSerializer, serializers.ModelSerializer):
    """Serializer for Announcement model."""

    tags = TagListSerializerField()
    author: HyperlinkedRelatedField = serializers.HyperlinkedRelatedField(
        view_name="api:profile-detail", lookup_field="username", read_only=True
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
