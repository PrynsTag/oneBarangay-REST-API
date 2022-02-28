"""Create your announcement models here."""
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
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

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

    CIVIL_STATUS_CHOICES = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Widowed", "Widowed"),
        ("Separated", "Separated"),
        ("Divorced", "Divorced"),
        ("Annulled", "Annulled"),
        ("Cohabiting", "Cohabiting"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
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
        max_length=255,
        blank=True,
        choices=CIVIL_STATUS_CHOICES,
        default="Single",
    )

    def __str__(self):
        """Profile model string representation."""
        return f"{self.user.username.capitalize()}'s Profile"

    def save(self, *args, **kwargs):
        """Override save method to add username to profile."""
        self.username = self.user.username
        super().save(*args, **kwargs)
