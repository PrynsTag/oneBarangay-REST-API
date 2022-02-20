"""Create your rbi factories here."""
from zoneinfo import ZoneInfo

import factory
from factory.django import DjangoModelFactory

from onebarangay_psql.rbi.models import FamilyMember, HouseRecord


class HouseRecordFactory(DjangoModelFactory):
    """HouseRecord factory."""

    house_id = factory.Faker("random_number", digits=5)
    date_accomplished = factory.Faker(
        "date_time_between",
        start_date="-3y",
        end_date="now",
        tzinfo=ZoneInfo("Asia/Manila"),
    )
    address = factory.Faker("address")
    family_name = factory.Faker("last_name")
    street = factory.Faker("street_name")

    class Meta:
        """Meta class for HouseRecordFactory."""

        model = HouseRecord
        django_get_or_create = ["house_id"]


class FamilyMemberFactory(DjangoModelFactory):
    """FamilyMember factory."""

    house_record = factory.SubFactory(HouseRecordFactory)
    family_member_id = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    middle_name = factory.Faker("last_name")
    last_name = house_record.get_factory().family_name
    age = factory.Faker("random_number", digits=2)
    birth_place = factory.Faker("city")
    citizenship = factory.Faker(
        "random_element",
        elements=[
            "Filipino",
            "American",
            "Japanese",
            "Chinese",
            "Korean",
            "Singaporean",
        ],
    )
    civil_status = factory.Faker(
        "random_element", elements=["SI", "MD", "WD", "SP", "DV", "CH"]
    )
    date_of_birth = factory.Faker(
        "date_time_between",
        start_date="-60y",
        end_date="now",
        tzinfo=ZoneInfo("Asia/Manila"),
    )
    extension = factory.Faker("prefix")
    monthly_income = factory.Faker("random_number", digits=6)
    remarks = factory.Faker(
        "random_element",
        elements=[
            "Father",
            "Mother",
            "Son",
            "Daughter",
            "Grandfather",
            "Grandmother",
            "Uncle",
            "Aunt",
            "Nephew",
            "Niece",
            "Cousin",
        ],
    )
    gender = factory.Faker("random_element", elements=["M", "F", "N", "O"])

    class Meta:
        """Meta class for FamilyMemberFactory."""

        model = FamilyMember
        django_get_or_create = ["family_member_id"]
