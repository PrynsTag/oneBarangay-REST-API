"""Create your app config for user apps."""
import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    """Create your app config for user apps."""

    name = "onebarangay_psql.users"
    verbose_name = _("Users")

    @staticmethod
    def ready():
        """Import signal handlers."""
        # pylint: disable=C0415,W0611
        with contextlib.suppress(ImportError):
            import onebarangay_psql.users.signals  # noqa: F401
