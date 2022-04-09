"""Register your appointment models here."""
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from onebarangay_psql.appointment.models import Appointment


class AppointmentResource(resources.ModelResource):
    """Register your appointment models here."""

    class Meta:
        """Register your appointment models here."""

        model = Appointment
        skip_unchanged = True
        report_skipped = False
        exclude = ("government_id",)
        export_order = (
            "id",
            "created_at",
            "updated_at",
            "user",
            "recipient_name",
            "purpose",
            "start_appointment",
            "end_appointment",
            "status",
        )


class AppointmentAdmin(ImportExportModelAdmin):
    """Appointment Admin."""

    resource_class = AppointmentResource
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "user",
        "recipient_name",
        "purpose",
        "start_appointment",
        "end_appointment",
        "status",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "start_appointment",
        "end_appointment",
        "status",
    )
    list_per_page = 25
    list_max_show_all = 1000
    search_fields = ("recipient_name", "purpose", "user__username")
    ordering = ("-created_at", "-updated_at")


admin.site.register(Appointment, AppointmentAdmin)
