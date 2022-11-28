"""Create your announcement models here."""
from auditlog.registry import auditlog
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default custom user model for oneBarangay PostgreSQL.

    If adding fields that need to be filled at user signup, check forms.SignupForm and forms.SocialSignupForms
    accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    # name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    class Meta:
        """Meta class for User model."""

        ordering = ["-id"]
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        """User model string representation."""
        return self.username

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"username": self.username})


class Profile(models.Model):
    """Profile model for user's profile data."""

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

    user = models.OneToOneField(User, on_delete=models.CASCADE, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(
        upload_to="profile_pics",
        blank=True,
        default="profile_pics/default.jpg",
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        help_text="Lot/Blk/Phase Floor Number, building name or Apartment name,  "
        "street name, barangay, city, province, zipcode",
    )
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+639123456789'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    age = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(10), MaxValueValidator(100)],
    )
    birth_place = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    civil_status = models.CharField(
        _("Civil Status"),
        max_length=2,
        choices=CivilStatus.choices,
        default=CivilStatus.SINGLE,
    )
    gender = models.CharField(
        _("Gender"), max_length=1, choices=Gender.choices, blank=True
    )

    class Meta:
        """Meta class for Profile model."""

        ordering = ["-id"]
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        """Profile model string representation."""
        return f"{self.user.username.capitalize()}'s Profile"


auditlog.register(User)
auditlog.register(Profile)
