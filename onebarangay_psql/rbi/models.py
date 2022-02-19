"""Create your rbi models here."""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class HouseRecord(models.Model):
    """HouseRecord model."""

    house_id = models.CharField(_("House Number"), primary_key=True, max_length=255)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    date_accomplished = models.DateTimeField(
        _("Date Accomplished"),
    )
    address = models.CharField(_("Address"), max_length=255)
    family_name = models.CharField(_("Family Name"), max_length=100)
    street = models.CharField(_("Street"), max_length=255)

    class Meta:
        """Meta class for HouseRecord model."""

        ordering = ["-created_at", "-updated_at"]
        verbose_name = _("house record")
        verbose_name_plural = _("house records")

    def __str__(self):
        """Return string representation of appointment."""
        return f"{self.house_id}"


class FamilyMember(models.Model):
    """FamilyMember model."""

    class CivilStatus(models.TextChoices):
        """CivilStatus choices."""

        SINGLE = "SI", _("Single")
        MARRIED = "MD", _("Married")
        WIDOWED = "WD", _("Widowed")
        SEPARATED = "SP", _("Separated")
        DIVORCED = "DV", _("Divorced")
        COHABITING = "CH", _("Cohabiting")

    class Gender(models.TextChoices):
        """Gender Choices."""

        MALE = "M", _("Male")
        FEMALE = "F", _("Female")
        NON_BINARY = "N", _("Non-binary")
        OTHERS = "O", _("Others")

    house_id = models.ForeignKey(
        verbose_name=_("House Number"), to=HouseRecord, on_delete=models.CASCADE
    )
    family_member_id = models.AutoField(_("Family Member ID"), primary_key=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    first_name = models.CharField(_("First Name"), max_length=255)
    middle_name = models.CharField(_("Middle Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    age = models.PositiveIntegerField(
        _("Age"), validators=[MinValueValidator(1), MaxValueValidator(130)]
    )
    birth_place = models.CharField(_("Birth Place"), max_length=255)
    citizenship = models.CharField(_("Citizenship"), max_length=255)
    civil_status = models.CharField(
        _("Civil Status"),
        max_length=2,
        choices=CivilStatus.choices,
        default=CivilStatus.SINGLE,
    )
    date_of_birth = models.DateTimeField(
        _("Date of Birth"),
    )
    extension = models.CharField(_("Extension"), max_length=255)
    monthly_income = models.PositiveIntegerField(
        _("Monthly Income"),
    )
    remarks = models.CharField(_("Remarks"), max_length=255)
    gender = models.CharField(_("Gender`"), max_length=1, choices=Gender.choices)

    class Meta:
        """Meta class for FamilyMember model."""

        ordering = ["-created_at", "-updated_at"]
        verbose_name = _("family member")
        verbose_name_plural = _("family members")

    def __str__(self):
        """Return string representation of rbi."""
        return f"{self.house_id}. {self.first_name} {self.last_name}"
