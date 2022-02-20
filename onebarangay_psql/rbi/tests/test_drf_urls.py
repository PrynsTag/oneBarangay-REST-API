"""Create your rbi drf urls tests here."""
from django.urls import resolve
from rest_framework.reverse import reverse

from onebarangay_psql.rbi.models import FamilyMember


class TestHouseRecordViewSetUrls:
    """Test HouseRecordViewSet urls."""

    def test_house_record_list(self):
        """Test house record list url."""
        assert reverse("api:house-list") == "/api/house-record/"
        assert resolve("/api/house-record/").view_name == "api:house-list"

    def test_house_record_detail(self, house_record):
        """Test house record detail url.

        Args:
            house_record (HouseRecord): The house record object to test.
        """
        assert (
            reverse("api:house-detail", kwargs={"pk": house_record.house_id})
            == f"/api/house-record/{house_record.house_id}/"
        )
        assert (
            resolve(f"/api/house-record/{house_record.house_id}/").view_name
            == "api:house-detail"
        )


class TestFamilyMemberViewSetUrls:
    """Test FamilyMemberViewSet urls."""

    def test_family_member_list(self):
        """Test family member list url."""
        assert reverse("api:family-list") == "/api/family-member/"
        assert resolve("/api/family-member/").view_name == "api:family-list"

    def test_family_member_detail(self, family_member: FamilyMember):
        """Test family member detail url.

        Args:
            family_member (FamilyMember): The family member object to test.
        """
        assert (
            reverse("api:family-detail", kwargs={"pk": family_member.family_member_id})
            == f"/api/family-member/{family_member.family_member_id}/"
        )
        assert (
            resolve(f"/api/family-member/{family_member.family_member_id}/").view_name
            == "api:family-detail"
        )
