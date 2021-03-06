"""Create your test factories here."""
from collections.abc import Sequence
from typing import Any

from django.contrib.auth import get_user_model
from factory import Faker, post_generation
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    """Create a user factory."""

    username = Faker("user_name")
    email = Faker("email")

    @post_generation
    # pylint: disable=unused-argument
    def password(self, create: bool, extracted: Sequence[Any], **kwargs: dict) -> None:
        """Set the password for the user.

        Args:
            create (bool): Whether to create the user.
            extracted (Sequence[Any]): The extracted password.
            **kwargs (dict): The keyword arguments.
        """
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    class Meta:
        """Meta class for User Factory."""

        model = get_user_model()
        django_get_or_create = ["username"]
