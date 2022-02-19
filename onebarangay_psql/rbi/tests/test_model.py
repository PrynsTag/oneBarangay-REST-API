"""Create your rbi model tests here."""
import datetime
from zoneinfo import ZoneInfo

from onebarangay_psql.rbi.models import FamilyMember, HouseRecord


class TestRBI:
    """Test the rbi model."""

    def test_create_rbi(self):
        """Test creating a rbi model.

        Scenario:
            - The code should be able to create a HouseRecord and FamilyMember model
        Returns:
            None
        """
        hr = HouseRecord.objects.create(
            house_id="1",
            date_accomplished=datetime.datetime(
                year=1990, month=1, day=1, tzinfo=ZoneInfo("Asia/Manila")
            ),
            address="Manila, Philippines",
            family_name="Velasco",
            street="San Antonio Street",
        )
        fm = FamilyMember.objects.create(
            house_id=hr,
            first_name="Prince",
            middle_name="Salonga",
            last_name=hr.family_name,
            age="26",
            birth_place="Manila",
            citizenship="Filipino",
            civil_status="S",
            date_of_birth=datetime.datetime(
                year=1990, month=1, day=1, tzinfo=ZoneInfo("Asia/Manila")
            ),
            extension="Dr.",
            monthly_income=100000,
            remarks="Son",
            gender="M",
        )

        assert hr.house_id == "1"
        assert fm.last_name == hr.family_name

    def test_house_record_str(self):
        """Test the HouseRecord string representation.

        Scenario:
            - The code should be able to output the HouseRecord model as a string
        Returns:
            None
        """
        hr = HouseRecord.objects.create(
            house_id="1",
            date_accomplished=datetime.datetime(
                year=1990, month=1, day=1, tzinfo=ZoneInfo("Asia/Manila")
            ),
            address="Manila, Philippines",
            family_name="Velasco",
            street="San Antonio Street",
        )

        assert str(hr) == "1"

    def test_family_member_str(self):
        """Test the FamilyMember string representation.

        Scenario:
            - The code should be able to output the FamilyMember model as a string
        Returns:
            None
        """
        hr = HouseRecord.objects.create(
            house_id="1",
            date_accomplished=datetime.datetime(
                year=1990, month=1, day=1, tzinfo=ZoneInfo("Asia/Manila")
            ),
            address="Manila, Philippines",
            family_name="Velasco",
            street="San Antonio Street",
        )

        fm = FamilyMember.objects.create(
            house_id=hr,
            first_name="Prince",
            middle_name="Salonga",
            last_name=hr.family_name,
            age="26",
            birth_place="Manila",
            citizenship="Filipino",
            civil_status="S",
            date_of_birth=datetime.datetime(
                year=1990, month=1, day=1, tzinfo=ZoneInfo("Asia/Manila")
            ),
            extension="Dr.",
            monthly_income=100000,
            remarks="Son",
            gender="M",
        )

        assert str(fm) == f"{fm.house_id}. {fm.first_name} {fm.last_name}"

    def test_update_hr(self):
        """Test updating HouseRecord model.

        Scenario:
            - The code should be able to update the HouseRecord model
        Returns:
            None
        """
        hr = HouseRecord.objects.create(
            house_id="1",
            date_accomplished=datetime.datetime(
                year=1990, month=1, day=1, tzinfo=ZoneInfo("Asia/Manila")
            ),
            address="Manila, Philippines",
            family_name="Velasco",
            street="San Antonio Street",
        )

        hr.street = "San Martino Street"

        assert hr.street == "San Martino Street"

    def test_update_fm(self):
        """Test updating FamilyMember model.

        Scenario:
            - The code should be able to update the FamilyMember model
        Returns:
            None
        """
        hr = HouseRecord.objects.create(
            house_id="1",
            date_accomplished=datetime.datetime(
                year=1990, month=1, day=1, tzinfo=ZoneInfo("Asia/Manila")
            ),
            address="Manila, Philippines",
            family_name="Velasco",
            street="San Antonio Street",
        )

        fm = FamilyMember.objects.create(
            house_id=hr,
            first_name="Prince",
            middle_name="Salonga",
            last_name=hr.family_name,
            age=26,
            birth_place="Manila",
            citizenship="Filipino",
            civil_status="S",
            date_of_birth=datetime.datetime(
                year=1990, month=1, day=1, tzinfo=ZoneInfo("Asia/Manila")
            ),
            extension="Dr.",
            monthly_income=100000,
            remarks="Son",
            gender="M",
        )

        fm.age = 27

        assert fm.age == 27

    def test_hr_ordering(self):
        """Test the HouseRecord ordering.

        Scenario:
            - The code should output the proper ordering of HouseRecord model (Last created model should be first)
        Returns:
            None
        """
        hr1 = HouseRecord.objects.create(
            house_id="1",
            date_accomplished=datetime.datetime.now(tz=ZoneInfo("Asia/Manila")),
            address="Manila, Philippines",
            family_name="Velasco",
            street="San Antonio Street",
        )

        hr2 = HouseRecord.objects.create(
            house_id="2",
            date_accomplished=datetime.datetime.now(tz=ZoneInfo("Asia/Manila")),
            address="Manila, Philippines",
            family_name="Velasco",
            street="San Antonio Street",
        )

        assert HouseRecord.objects.all()[0] == hr2
        assert HouseRecord.objects.all()[1] == hr1

    def test_fm_ordering(self):
        """Test the FamilyMember ordering.

        Scenario:
            - The code should output the proper ordering of FamilyMember model (Last created model should be first)
        Returns:
            None
        """
        hr = HouseRecord.objects.create(
            house_id="1",
            date_accomplished=datetime.datetime(
                year=1990, month=1, day=1, tzinfo=ZoneInfo("Asia/Manila")
            ),
            address="Manila, Philippines",
            family_name="Velasco",
            street="San Antonio Street",
        )

        fm1 = FamilyMember.objects.create(
            house_id=hr,
            first_name="Prince",
            middle_name="Salonga",
            last_name=hr.family_name,
            age=26,
            birth_place="Manila",
            citizenship="Filipino",
            civil_status="S",
            date_of_birth=datetime.datetime(
                year=1990, month=1, day=1, tzinfo=ZoneInfo("Asia/Manila")
            ),
            extension="Dr.",
            monthly_income=100000,
            remarks="Son",
            gender="M",
        )

        fm2 = FamilyMember.objects.create(
            house_id=hr,
            first_name="Princess",
            middle_name="Salonga",
            last_name=hr.family_name,
            age=26,
            birth_place="Manila",
            citizenship="Filipino",
            civil_status="S",
            date_of_birth=datetime.datetime(
                year=1990, month=1, day=1, tzinfo=ZoneInfo("Asia/Manila")
            ),
            extension="Dr.",
            monthly_income=100000,
            remarks="Son",
            gender="M",
        )

        assert FamilyMember.objects.all()[0] == fm2
        assert FamilyMember.objects.all()[1] == fm1
