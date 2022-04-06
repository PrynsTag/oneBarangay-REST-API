"""Create your app config for announcement apps."""
import contextlib

from django.apps import AppConfig


class AnnouncementConfig(AppConfig):
    """Create your app config for announcement apps."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "onebarangay_psql.announcement"

    def ready(self):
        """Import signal handlers."""
        # pylint: disable=C0415,W0611
        with contextlib.suppress(ImportError):
            import onebarangay_psql.announcement.signals  # noqa: F401
