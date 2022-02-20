"""Create your rbi viewsets here."""
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from onebarangay_psql.rbi.models import FamilyMember, HouseRecord
from onebarangay_psql.rbi.serializers import (
    FamilyMemberSerializer,
    HouseRecordSerializer,
)


class HouseRecordViewSet(viewsets.ModelViewSet):
    """HouseRecord viewset."""

    queryset = HouseRecord.objects.all()
    serializer_class = HouseRecordSerializer
    permission_classes = [IsAdminUser]


class FamilyMemberViewSet(viewsets.ModelViewSet):
    """FamilyMember viewset."""

    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer
    permission_classes = [IsAdminUser]
