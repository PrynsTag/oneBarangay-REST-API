"""Register your rbi models here."""
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from onebarangay_psql.rbi.models import FamilyMember, HouseRecord


class HouseRecordResource(resources.ModelResource):
    """House Record Resource for import and export model fields."""

    class Meta:
        """Meta class for HouseRecordResource."""

        model = HouseRecord
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ("house_id",)
        fields = (
            "house_id",
            "created_at",
            "updated_at",
            "date_accomplished",
            "address",
            "family_name",
            "street",
        )
        export_order = (
            "house_id",
            "created_at",
            "updated_at",
            "date_accomplished",
            "address",
            "family_name",
            "street",
        )


class HouseRecordAdmin(ImportExportModelAdmin):
    """House Record Admin Integration for import and export."""

    resource_class = HouseRecordResource
    list_display = (
        "house_id",
        "created_at",
        "updated_at",
        "date_accomplished",
        "address",
        "family_name",
        "street",
    )
    list_filter = ("created_at", "updated_at", "date_accomplished")
    search_fields = ("house_id", "family_name", "street")
    ordering = ("-created_at", "-updated_at")
    list_per_page = 25
    list_max_show_all = 1000
    list_select_related = True


class FamilyRecordResource(resources.ModelResource):
    """Family Record Resource for import and export model fields."""

    class Meta:
        """Meta class for FamilyRecordResource."""

        model = FamilyMember
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ("family_member_id",)
        fields = (
            "family_member_id",
            "created_at",
            "updated_at",
            "first_name",
            "middle_name",
            "last_name",
            "age",
            "birth_place",
            "citizenship",
            "civil_status",
            "date_of_birth",
            "monthly_income",
            "remarks",
            "gender",
        )
        export_order = (
            "family_member_id",
            "created_at",
            "updated_at",
            "first_name",
            "middle_name",
            "last_name",
            "age",
            "birth_place",
            "citizenship",
            "civil_status",
            "date_of_birth",
            "monthly_income",
            "remarks",
            "gender",
        )


class FamilyRecordAdmin(ImportExportModelAdmin):
    """Family Record Admin Custom Configuration."""

    resource_class = FamilyRecordResource
    list_display = (
        "family_member_id",
        "created_at",
        "updated_at",
        "first_name",
        "middle_name",
        "last_name",
        "age",
        "birth_place",
        "citizenship",
        "civil_status",
        "date_of_birth",
        "monthly_income",
        "remarks",
        "gender",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "date_of_birth",
        "gender",
        "citizenship",
        "civil_status",
    )
    search_fields = ("family_member_id", "first_name", "middle_name", "last_name")
    ordering = ("-created_at", "-updated_at")
    list_per_page = 25
    list_max_show_all = 1000
    list_select_related = True


admin.site.register(HouseRecord, HouseRecordAdmin)
admin.site.register(FamilyMember, FamilyRecordAdmin)
