"""Register your user models here.."""
from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from django.utils.translation import gettext as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from onebarangay_psql.users.forms import UserAdminChangeForm, UserAdminCreationForm
from onebarangay_psql.users.models import Profile


User = get_user_model()


class ProfileResource(resources.ModelResource):
    """Profile Resource for importing and exporting Profile Model fields."""

    class Meta:
        """Meta class for Profile Resource."""

        model = Profile
        skip_unchanged = True
        report_skipped = False
        fields = (
            "id",
            "created_at",
            "updated_at",
            "user",
            "first_name",
            "middle_name",
            "last_name",
            "address",
            "phone_number",
            "age",
            "birth_place",
            "birth_date",
            "civil_status",
            "gender",
        )


@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    """Profile Admin Custom Configuration."""

    resources_class = ProfileResource
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "user",
        "first_name",
        "middle_name",
        "last_name",
        "age",
        "gender",
        "phone_number",
        "address",
        "birth_place",
        "birth_date",
        "civil_status",
    )
    list_filter = ("created_at", "updated_at", "gender", "birth_date", "civil_status")
    search_fields = ("user__username", "first_name", "middle_name", "last_name")
    ordering = ("-created_at", "-updated_at")
    list_per_page = 25
    list_max_show_all = 1000
    list_select_related = True


class ProfileInline(admin.StackedInline):
    """Profile Inline Custom Configuration."""

    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"


class UserResource(resources.ModelResource):
    """User Resource for importing and exporting User Model fields."""

    class Meta:
        """Meta class for User Resource."""

        model = User
        skip_unchanged = True
        report_skipped = False
        fields = (
            "id",
            "username",
            "email",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        )


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin, ImportExportModelAdmin):
    """User Admin Custom Configuration."""

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    resource_class = UserResource
    ordering = ("-date_joined",)
    inlines = (ProfileInline,)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["email", "username", "is_superuser", "is_staff", "is_active"]
    list_per_page = 25
    list_max_show_all = 1000
    search_fields = ["username"]
