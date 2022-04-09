"""Create your own signals for your user's model."""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import strip_tags
from push_notifications.models import GCMDevice

from onebarangay_psql.announcement.models import Announcement


@receiver(post_save, sender=Announcement)
def notify_user_on_create_announcement(
    sender, instance: Announcement, created, **kwargs
):  # pylint: disable=unused-argument
    """Send a notification for every announcement created.

    Args:
        sender (class): The class of the model that is being saved.
        instance (object): The instance of the model that is being saved.
        created (bool): Whether the model is being created or updated.
        **kwargs (dict): Additional keyword arguments.
    """
    if created:
        GCMDevice.objects.all().send_message(
            message={
                "title": f"{instance.title}",
                "body": strip_tags(instance.content),
            }
        )
