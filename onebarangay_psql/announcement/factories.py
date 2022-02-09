"""Create your announcement factories here."""
import factory
from django.utils.text import slugify
from factory import Faker
from factory.django import DjangoModelFactory

from onebarangay_psql.announcement import models
from onebarangay_psql.users.factories import UserFactory


class AnnouncementFactory(DjangoModelFactory):
    """Announcement factory."""

    title = Faker("sentence", nb_words=6, variable_nb_words=True)
    content = Faker("text", max_nb_chars=200)
    author = factory.SubFactory(UserFactory)
    author_id = factory.LazyAttribute(lambda o: o.author.id)
    tags = Faker("words", nb=3)
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))

    class Meta:
        """Meta class for Announcement Factory."""

        model = models.Announcement
        django_get_or_create = ["slug"]
