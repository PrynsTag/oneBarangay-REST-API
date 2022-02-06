"""Register your user models here.."""
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from onebarangay_psql.users.forms import UserAdminChangeForm, UserAdminCreationForm
from onebarangay_psql.users.models import Profile

User = get_user_model()

admin.site.register(Profile)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    """User Admin Custom Configuration."""

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
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
    list_display = ["email", "username", "name", "is_superuser"]
    search_fields = ["name"]
