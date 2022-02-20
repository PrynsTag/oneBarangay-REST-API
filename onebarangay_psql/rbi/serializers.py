"""Create your rbi serializers here."""
from rest_framework import serializers

from onebarangay_psql.rbi.models import FamilyMember, HouseRecord
from onebarangay_psql.utils.choice_field import ChoicesField


class HouseRecordSerializer(serializers.ModelSerializer):
    """House record serializer."""

    class Meta:
        """Meta class for HouseRecordSerializer."""

        model = HouseRecord
        fields = "__all__"


class FamilyMemberSerializer(serializers.ModelSerializer):
    """Serializer for FamilyMember model."""

    house_record = HouseRecordSerializer
    civil_status = ChoicesField(choices=FamilyMember.CivilStatus.choices)
    gender = ChoicesField(choices=FamilyMember.Gender.choices)

    class Meta:
        """Meta class for FamilyMemberSerializer."""

        model = FamilyMember
        fields = "__all__"
