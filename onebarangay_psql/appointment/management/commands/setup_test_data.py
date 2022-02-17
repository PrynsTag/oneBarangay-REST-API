"""Create your custom management commands here."""
import random
from typing import Union

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import connection, transaction
from django.db.models import Max

from onebarangay_psql.announcement.factories import AnnouncementFactory
from onebarangay_psql.announcement.models import Announcement
from onebarangay_psql.appointment.factories import AppointmentFactory
from onebarangay_psql.appointment.models import Appointment
from onebarangay_psql.users.factories import UserFactory

NUM_USERS = 50
NUM_APPOINTMENTS = 25
NUM_APPOINTMENTS_PER_USER = 4
NUM_ANNOUNCEMENTS = 25
NUM_ANNOUNCEMENTS_PER_USER = 5

User = get_user_model()


# mypy: ignore-errors
class Command(BaseCommand):
    """Create your custom management commands here."""

    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        """Create your custom management commands here."""
        self.stdout.write("Deleting old data...")
        models: Union[Appointment, Announcement, User] = [
            Appointment,
            Announcement,
            User,
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating test and superuser account...")
        User.objects.create_superuser("prince", "prince@onebarangay.com", "prynstag")
        User.objects.create_user("test", "test@onebarangay.com", "prynstag")

        self.stdout.write("Creating new data...")
        # Create all the users
        people = []
        for _ in range(NUM_USERS):
            person = UserFactory()
            person.profile.phone_number = f"09{random.randint(1000000, 9999999)}"
            people.append(person)

        # Add users as announcers
        for _ in range(NUM_ANNOUNCEMENTS):
            announcers = random.choices(people, k=NUM_ANNOUNCEMENTS_PER_USER)
            #  pylint: disable=expression-not-assigned
            [AnnouncementFactory(author=announcer) for announcer in announcers]

        # Add users as appointees
        for _ in range(NUM_APPOINTMENTS):
            appointee = random.choices(people, k=NUM_APPOINTMENTS_PER_USER)
            #  pylint: disable=expression-not-assigned
            [AppointmentFactory(user=user) for user in appointee]

        self.stdout.write("Resetting indexes...")
        for m in models:
            set_sequence(m)


# mypy: ignore-errors
def set_sequence(model: Union[Appointment, Announcement, User]) -> None:
    """Reset the id sequence of a table.

    Args:
        model (Model): The model to reset the sequence of.
    Returns:
        None
    """
    max_id = model.objects.aggregate(m=Max("id"))["m"]
    seq = max_id or 1
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT setval(pg_get_serial_sequence(%s,'id'), %s);",
            [model._meta.db_table, seq],
        )
