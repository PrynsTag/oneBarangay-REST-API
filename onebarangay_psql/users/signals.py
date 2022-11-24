"""Create your own signals for your user's model."""
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from onebarangay_psql.users.models import Profile


User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(
    sender, instance, created, **kwargs
):  # pylint: disable=unused-argument
    """Create a profile for every new user.

    Args:
        sender (class): The class of the model that is being saved.
        instance (object): The instance of the model that is being saved.
        created (bool): Whether the model is being created or updated.
        **kwargs (dict): Additional keyword arguments.
    """
    if created:
        Profile.objects.create(user=instance)
