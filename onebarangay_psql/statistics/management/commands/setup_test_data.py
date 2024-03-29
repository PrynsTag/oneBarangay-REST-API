"""Create your custom management commands here."""
import random
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Union
from zoneinfo import ZoneInfo

from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import connection, transaction
from django.db.models import Max

from config.settings.base import APPS_DIR
from onebarangay_psql.announcement.factories import AnnouncementFactory
from onebarangay_psql.announcement.models import Announcement
from onebarangay_psql.appointment.factories import AppointmentFactory
from onebarangay_psql.appointment.models import Appointment
from onebarangay_psql.rbi.factories import FamilyMemberFactory, HouseRecordFactory
from onebarangay_psql.rbi.models import FamilyMember, HouseRecord
from onebarangay_psql.users.factories import UserFactory
from onebarangay_psql.users.models import Profile
from onebarangay_psql.utils.refresh_material_view import refresh_mv


NUM_USERS = 50
NUM_APPOINTMENTS = 25
NUM_APPOINTMENTS_PER_USER = 4
NUM_ANNOUNCEMENTS = 25
NUM_ANNOUNCEMENTS_PER_USER = 5
NUM_HOUSE = 25

User = get_user_model()


# mypy: ignore-errors
class Command(BaseCommand):
    """Create your custom management commands here."""

    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        """Create your custom management commands here."""
        self.stdout.write("Deleting old data...")
        models = [
            Appointment,
            Announcement,
            User,
            HouseRecord,
            FamilyMember,
        ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating test and superuser account...")
        User.objects.create_superuser("prince", "prince@onebarangay.com", "prynstag")
        EmailAddress.objects.create(
            user=User.objects.get(username="prince"),
            email="prince@onebarangay.com",
            primary=True,
            verified=True,
        )

        prince = Profile.objects.get(user__username="prince")
        prince.first_name = "Prince"
        prince.middle_name = "Salonga"
        prince.last_name = "Velasco"
        prince.gender = "M"
        prince.civil_status = "SI"
        prince.birth_date = date(2000, 1, 16)
        prince.address = "San Mateo, Rizal"
        prince.phone_number = "09171234567"
        today = date.today()
        age = (
            today.year
            - prince.birth_date.year
            - (
                (today.month, today.day)
                < (prince.birth_date.month, prince.birth_date.day)
            )
        )
        prince.age = age
        prince.birth_place = "Marikina City"
        prince.save()

        User.objects.create_user("test", "test@onebarangay.com", "prynstag")
        EmailAddress.objects.create(
            user=User.objects.get(username="test"),
            email="test@onebarangay.com",
            primary=True,
            verified=True,
        )
        self.stdout.write("Creating new data...")

        people = []
        last_six_months = datetime.now() - timedelta(days=30 * 6)
        for _ in range(NUM_USERS):
            user = UserFactory()
            user.last_login = (
                random.choice(
                    gen_time_between_days(last_six_months, back_to_past=True)
                ),
            )
            user.date_joined = (
                random.choice(
                    gen_time_between_days(last_six_months, back_to_past=True)
                ),
            )
            people.append(user)
            EmailAddress.objects.create(
                user=User.objects.get(username=user.username),
                email=user.email,
                primary=True,
                verified=True,
            )

        # Add users as announcers
        for person in random.choices(people, k=NUM_ANNOUNCEMENTS_PER_USER):
            AnnouncementFactory.create_batch(size=NUM_ANNOUNCEMENTS, author=person)

        # Add users as appointees
        for person in random.choices(people, k=NUM_APPOINTMENTS_PER_USER):
            AppointmentFactory.create_batch(size=NUM_APPOINTMENTS, user=person)

        houses = HouseRecordFactory.create_batch(size=NUM_HOUSE)
        for house in houses:
            FamilyMemberFactory.create_batch(
                size=random.randrange(2, 6),
                house_record=house,
                last_name=house.family_name,
            )

        # Refresh materialized views
        refresh_mv()

        self.stdout.write("Resetting indexes...")
        for m in models:
            set_sequence(m)

        self.stdout.write("Deleting old images...")
        delete_all_media_files()


def set_sequence(
    model: Union[Appointment, Announcement, User, HouseRecord, FamilyMember]
) -> None:
    """Reset the id sequence of a table.

    Args:
        model (Model): The model to reset the sequence of.
    Returns:
        None
    """
    if model == HouseRecord:
        model_id = "house_id"
    elif model == FamilyMember:
        model_id = "family_member_id"
    else:
        model_id = "id"

    max_id = model.objects.aggregate(m=Max(model_id))["m"]
    seq = max_id or 1
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT setval(pg_get_serial_sequence(%s,%s), %s);",
            [model._meta.db_table, model_id, seq],
        )


def delete_all_media_files():
    """Delete all media files.

    Returns:
        None
    """
    appointment_media_path = Path(APPS_DIR / "media/appointment/government_id")
    announcement_media_path = Path(APPS_DIR / "media/announcement/thumbnail")
    profile_media_path = Path(APPS_DIR / "media/profile_pics")

    for path in [
        appointment_media_path,
        announcement_media_path,
        profile_media_path,
    ]:
        for f in path.iterdir():
            if (
                not f.name.startswith(".")
                and f.is_file()
                and f.suffix in [".jpg", ".png"]
                and f.name != "default.png"
                and f.name != "default.jpg"
            ):
                f.unlink()


def gen_time_between_days(
    end: datetime,
    start: datetime = None,
    num_days: int = 7,
    back_to_past: bool = False,
) -> list[datetime]:
    """Generate a list of random datetime objects between two dates.

    Args:
        start (datetime, optional): The start date. Defaults to datetime.datetime.now().
        end (datetime): The end date.
        num_days (int, optional): The number of days to generate. Defaults to 7.
        back_to_past (bool): Whether to generate dates back to the past. Defaults to False.
    Returns:
        list[datetime]: A list of datetime objects.
    """
    if start is None:
        start = datetime.now()

    start_dt_aware = start.astimezone(tz=ZoneInfo("Asia/Manila"))
    random_second = random.randint(0, abs(int((end - start).total_seconds())))
    if back_to_past:
        random_date = start_dt_aware - timedelta(seconds=random_second)

    else:
        random_date = start_dt_aware + timedelta(seconds=random_second)

    return [random_date for i in range(num_days)]
