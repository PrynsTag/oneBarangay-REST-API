"""Register your announcement models here."""
from django.contrib import admin
from django.utils.html import strip_tags
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from onebarangay_psql.announcement.models import Announcement


class AnnouncementResource(resources.ModelResource):
    """Announcement Resource for import and export model fields."""

    class Meta:
        """Meta class for Announcement Resource."""

        model = Announcement
        skip_unchanged = True
        report_skipped = False
        exclude = ("thumbnail", "slug")
        export_order = (
            "id",
            "author",
            "title",
            "tags",
            "content",
            "is_featured",
            "created_at",
            "updated_at",
        )


class AnnouncementAdmin(ImportExportModelAdmin):
    """Announcement Admin Integration for import and export."""

    list_display = (
        "id",
        "author",
        "title",
        "tag_list",
        "raw_content",
        "is_featured",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "content", "tags", "author__username")
    ordering = ("-created_at", "-updated_at")
    list_filter = ("created_at", "updated_at", "is_featured", "author", "tags")
    list_per_page = 25
    list_max_show_all = 1000
    prepopulated_fields = {"slug": ("title",)}
    resource_class = AnnouncementResource

    def get_queryset(self, request):
        """Get the queryset of Announcement Model."""
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        """Return the tags as a comma separated string."""
        return ", ".join(o.name for o in obj.tags.all())

    def raw_content(self, obj):
        """Return the content without html."""
        return strip_tags(obj.content)


admin.site.register(Announcement, AnnouncementAdmin)
