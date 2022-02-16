"""Create your appointment factories here."""
from zoneinfo import ZoneInfo

import factory
from django.core.files.uploadedfile import SimpleUploadedFile
from factory.django import DjangoModelFactory

from config.settings.base import APPS_DIR
from onebarangay_psql.appointment.models import Appointment
from onebarangay_psql.users.factories import UserFactory

with open(APPS_DIR / "media/appointment/government_id/default.png", "rb") as f:
    image = SimpleUploadedFile(f.name, f.read(), content_type="image/jpeg")


class AppointmentFactory(DjangoModelFactory):
    """Appointment factory."""

    id = factory.Sequence(lambda n: n)
    user = factory.SubFactory(UserFactory)
    recipient_name = factory.Faker("name")
    purpose = factory.Faker("text", max_nb_chars=200)
    government_id = image
    start_appointment = factory.Faker(
        "date_time_this_century",
        before_now=True,
        after_now=False,
        tzinfo=ZoneInfo("Asia/Manila"),
    )
    status = factory.Faker("random_element", elements=Appointment.Status.values)
    document = factory.Faker("random_element", elements=Appointment.Document.values)

    class Meta:
        """Meta class for appointment factory."""

        model = Appointment
        django_get_or_create = ["id"]
