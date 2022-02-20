"""Create your rbi drf http methods tests here."""
import datetime
from zoneinfo import ZoneInfo

from django.test.client import Client
from django.urls import reverse
from rest_framework import status

from onebarangay_psql.rbi.models import FamilyMember, HouseRecord


class TestHouseRecordViewSetUrls:
    """Create your rbi drf http methods tests here."""

    def test_house_record_list(self, admin_api_client: Client):
        """Test house record list.

        Scenario:
            - As an admin user, I should be able to access the house record list
        Args:
            admin_api_client (Client): The admin api client making the get request
        """
        response = admin_api_client.get(reverse("api:house-list"))
        assert response.status_code == status.HTTP_200_OK

    def test_house_record_retrieve(
        self, admin_api_client: Client, house_record: HouseRecord
    ):
        """Test house record retrieve.

        Scenario:
            - As an admin user, I should be able to access a specific house record
        Args:
            admin_api_client (Client): The admin api client making the get request
            house_record (HouseRecord): The house record to be retrieved
        """
        response = admin_api_client.get(
            reverse("api:house-detail", kwargs={"pk": house_record.pk})
        )
        assert response.status_code == status.HTTP_200_OK

    def test_house_record_post(self, admin_api_client: Client):
        """Test house record post.

        Scenario:
            - As an admin user, I should be able to create a new house record
        Args:
            admin_api_client (Client): The admin api client making the post request
        """
        response = admin_api_client.post(
            reverse("api:house-list"),
            {
                "house_id": "1",
                "date_accomplished": datetime.datetime.now(tz=ZoneInfo("Asia/Manila")),
                "address": "Manila, Philippines",
                "family_name": "Velasco",
                "street": "San Antonio Street",
            },
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_house_record_put(
        self, admin_api_client: Client, house_record: HouseRecord
    ):
        """Test house record put.

        Scenario:
            - As an admin user, I should be able to update a house record
        Args:
            admin_api_client (Client): The admin api client making the put request
            house_record (HouseRecord): The house record to be updated
        """
        response = admin_api_client.put(
            reverse("api:house-detail", kwargs={"pk": house_record.house_id}),
            {
                "house_id": house_record.house_id,
                "date_accomplished": house_record.date_accomplished,
                "address": "Manila, Philippines",
                "family_name": house_record.family_name,
                "street": house_record.street,
            },
        )

        # Turn response.content into a dict
        response_dict = response.json()
        assert response_dict["address"] == "Manila, Philippines"
        assert response.status_code == status.HTTP_200_OK

    def test_house_record_patch(
        self, admin_api_client: Client, house_record: HouseRecord
    ):
        """Test house record patch.

        Scenario:
            - As an admin user, I should be able to partially update a house record
        Args:
            admin_api_client (Client): The admin api client making the patch request
            house_record (HouseRecord): The house record to be partially updated
        """
        response = admin_api_client.patch(
            reverse("api:house-detail", kwargs={"pk": house_record.house_id}),
            {"address": "Manila, Philippines"},
        )
        response_dict = response.json()
        assert response_dict["address"] == "Manila, Philippines"
        assert response.status_code == status.HTTP_200_OK

    def test_house_record_delete(
        self, admin_api_client: Client, house_record: HouseRecord
    ):
        """Test house record delete.

        Scenario:
            - As an admin user, I should be able to delete a house record
        Args:
            admin_api_client (Client): The admin api client making the delete request
            house_record (HouseRecord): The house record to be deleted
        """
        response = admin_api_client.delete(
            reverse("api:house-detail", kwargs={"pk": house_record.house_id})
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestFamilyMemberViewSet:
    """Create your rbi drf http methods tests here."""

    def test_family_member_list(self, admin_api_client: Client):
        """Test family member list.

        Scenario:
            - As an admin user, I should be able to access the list of family members
        Args:
            admin_api_client (Client): The admin api client making the get request
        """
        response = admin_api_client.get(reverse("api:family-list"))
        assert response.status_code == status.HTTP_200_OK

    def test_family_member_retrieve(
        self, admin_api_client: Client, family_member: FamilyMember
    ):
        """Test family member retrieve.

        Scenario:
            - As an admin user, I should be able to access a single family member
        Args:
            admin_api_client (Client): The admin api client making the get request
            family_member (FamilyMember): The family member to be retrieved
        """
        response = admin_api_client.get(
            reverse("api:family-detail", kwargs={"pk": family_member.pk})
        )
        assert response.status_code == status.HTTP_200_OK

    def test_family_member_post(
        self, admin_api_client: Client, house_record: HouseRecord
    ):
        """Test family member post.

        Scenario:
            - As an admin user, I should be able to create a family member
        Args:
            admin_api_client (Client): The admin api client making the post request
            house_record (HouseRecord): The house record to be used in the post request
        """
        response = admin_api_client.post(
            reverse("api:family-list"),
            {
                "house_record": house_record,
                "first_name": "Prince",
                "middle_name": "Salonga",
                "last_name": house_record.family_name,
                "age": 26,
                "birth_place": "Manila",
                "citizenship": "Filipino",
                "civil_status": "SI",
                "date_of_birth": datetime.datetime(
                    year=1990, month=1, day=1, tzinfo=ZoneInfo("Asia/Manila")
                ),
                "extension": "Dr.",
                "monthly_income": 100000,
                "remarks": "Son",
                "gender": "M",
            },
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_family_member_put(
        self,
        admin_api_client: Client,
        house_record: HouseRecord,
        family_member: FamilyMember,
    ):
        """Test family member put.

        Scenario:
            - As an admin user, I should be able to update a family member
        Args:
            admin_api_client (Client): The admin api client making the put request
            house_record (HouseRecord): The house record to be used in the put request
            family_member (FamilyMember): The family member to be updated
        """
        response = admin_api_client.put(
            reverse("api:family-detail", kwargs={"pk": family_member.family_member_id}),
            {
                "house_record": house_record,
                "first_name": family_member.first_name,
                "middle_name": family_member.middle_name,
                "last_name": house_record.family_name,
                "age": family_member.age,
                "birth_place": family_member.birth_place,
                "citizenship": family_member.citizenship,
                "civil_status": "MD",
                "date_of_birth": family_member.date_of_birth,
                "extension": family_member.extension,
                "monthly_income": family_member.monthly_income,
                "remarks": family_member.remarks,
                "gender": family_member.gender,
            },
        )
        response_dict = response.json()
        assert response_dict["civil_status"] == "Married"
        assert response.status_code == status.HTTP_200_OK

    def test_family_member_patch(
        self, admin_api_client: Client, family_member: FamilyMember
    ):
        """Test family member patch.

        Scenario:
            - As an admin user, I should be able to partially update a family member
        Args:
            admin_api_client (Client): The admin api client making the patch request
            family_member (FamilyMember): The family member to be partially updated
        """
        response = admin_api_client.patch(
            reverse("api:family-detail", kwargs={"pk": family_member.family_member_id}),
            {"civil_status": "MD"},
        )
        response_dict = response.json()
        assert response_dict["civil_status"] == "Married"
        assert response.status_code == status.HTTP_200_OK

    def test_family_member_delete(
        self, admin_api_client: Client, family_member: FamilyMember
    ):
        """Test family member delete.

        Args:
            admin_api_client (Client): The admin api client making the delete request
            family_member (FamilyMember): The family member to be deleted
        """
        response = admin_api_client.delete(
            reverse("api:family-detail", kwargs={"pk": family_member.family_member_id})
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
