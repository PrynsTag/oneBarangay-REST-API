"""Create your statistics models here."""
from django.db import models


class TotalMaterializedView(models.Model):
    """Totals Materialized View."""

    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=30)
    value = models.PositiveBigIntegerField()

    class Meta:
        """Meta class for TotalsMaterializedView."""

        managed = False
        ordering = ["id"]
        db_table = "materialized_statistics_total"

    def __str__(self):
        """Return String Representation of TotalsMaterializedView."""
        return self.label


class UserSignUpMaterializedView(models.Model):
    """User Signup Materialized View."""

    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    value = models.PositiveBigIntegerField()

    class Meta:
        """Meta class for UserSignUpMaterializedView."""

        managed = False
        ordering = ["id"]
        db_table = "materialized_statistics_user_signup"

    def __str__(self):
        """Return String Representation of UserSignUpMaterializedView."""
        return self.label


class AppointmentMaterializedView(models.Model):
    """Appointment Materialized View."""

    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=50)
    value = models.PositiveBigIntegerField()

    class Meta:
        """Meta class for AppointmentMaterializedView."""

        managed = False
        ordering = ["id"]
        db_table = "materialized_statistics_appointment"

    def __str__(self):
        """Return String Representation of AppointmentMaterializedView."""
        return self.label


class UserLogInMaterializedView(models.Model):
    """User Login Materialized View."""

    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=50)
    value = models.PositiveBigIntegerField()

    class Meta:
        """Meta class for UserLogInMaterializedView."""

        managed = False
        ordering = ["id"]
        db_table = "materialized_statistics_user_login"

    def __str__(self):
        """Return String Representation of UserLogInMaterializedView."""
        return self.label


class AgeGroupMaterializedView(models.Model):
    """Age group Materialized View."""

    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=50)
    value = models.PositiveBigIntegerField()
    total_age = models.IntegerField()

    class Meta:
        """Meta class for AgeGroupMaterializedView."""

        managed = False
        ordering = ["id"]
        db_table = "materialized_statistics_age_group"

    def __str__(self):
        """Return String Representation of AgeGroupMaterializedView."""
        return self.label


class CitizenshipMaterializedView(models.Model):
    """Citizenship Materialized View."""

    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=50)
    value = models.PositiveBigIntegerField()

    class Meta:
        """Meta class for CitizenshipMaterializedView."""

        managed = False
        ordering = ["id"]
        db_table = "materialized_statistics_citizenship"

    def __str__(self):
        """Return String Representation of CitizenshipMaterializedView."""
        return self.label


class CivilStatusMaterializedView(models.Model):
    """Civil Status Materialized View."""

    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=50)
    value = models.PositiveBigIntegerField()

    class Meta:
        """Meta class for CivilStatusMaterializedView."""

        managed = False
        ordering = ["id"]
        db_table = "materialized_statistics_civil_status"

    def __str__(self):
        """Return String Representation of CivilStatusMaterializedView."""
        return self.label


class AverageMaterializedView(models.Model):
    """Average Materialized View."""

    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=50)
    value = models.PositiveBigIntegerField()

    class Meta:
        """Meta class for AverageMaterializedView."""

        managed = False
        ordering = ["id"]
        db_table = "materialized_statistics_average"

    def __str__(self):
        """Return String Representation of AverageMaterializedView."""
        return self.label


class SocialClassMaterializedView(models.Model):
    """Average Materialized View."""

    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=50)
    value = models.PositiveBigIntegerField()
    max_income = models.PositiveBigIntegerField()

    class Meta:
        """Meta class for SocialClassMaterializedView."""

        managed = False
        ordering = ["id"]
        db_table = "materialized_statistics_social_class"

    def __str__(self):
        """Return String Representation of SocialClassMaterializedView."""
        return self.label


class RefreshMaterializedView(models.Model):
    """Refresh Materialized View."""

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    duration = models.DurationField(auto_created=True)

    class Meta:
        """Meta class for RefreshMaterializedView."""

        verbose_name = "refresh"
        verbose_name_plural = "refreshes"
        ordering = ["-created_at"]

    def __str__(self):
        """Return String Representation of RefreshMaterializedView."""
        return self.created_at
