"""Create your appointment models here."""
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Appointment(models.Model):
    """Appointment model."""

    INDIGENCY = "IND"
    VERIFICATION = "VER"
    LOCAL_EMPLOYMENT = "EMP"
    CLEARANCE_PERMIT = "CLP"
    FILE_ACTION = "CFA"
    COMPLAINT_FILING = "COF"
    FILE_COUNTERCLAIM = "CFC"
    BORROW = "BOR"
    APPOINTMENT = "APT"
    DOCUMENT_CHOICES = [
        (INDIGENCY, _("Indigency")),
        (VERIFICATION, _("Verification")),
        (LOCAL_EMPLOYMENT, _("Local Employment")),
        (CLEARANCE_PERMIT, _("Clearance Permit")),
        (FILE_ACTION, _("Certificate to File Action")),
        (COMPLAINT_FILING, _("Complaint Filing")),
        (FILE_COUNTERCLAIM, _("Certificate to File Counterclaim")),
        (BORROW, _("Borrowing of Tools and Equipment")),
        (APPOINTMENT, _("General Appointment")),
    ]

    PENDING = "PEN"
    APPROVED = "APP"
    REJECTED = "REJ"
    COMPLETED = "COM"
    CANCELLED = "CAN"
    STATUS_CHOICES = [
        (PENDING, _("Pending")),
        (APPROVED, _("Completed")),
        (CANCELLED, _("Cancelled")),
        (REJECTED, _("Rejected")),
        (APPROVED, _("Approved")),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipient_name = models.CharField(_("Name of Recipient"), max_length=255)
    purpose = models.TextField(_("Purpose"), max_length=500, blank=True)
    government_id = models.ImageField(
        _("Government I.D."), upload_to="appointment/government_id"
    )
    start_appointment = models.DateTimeField(_("Start Appointment"))
    end_appointment = models.DateTimeField(_("End Appointment"), blank=True, null=True)
    document = models.CharField(_("Document"), choices=DOCUMENT_CHOICES, max_length=3)
    status = models.CharField(
        _("Status"), choices=STATUS_CHOICES, max_length=3, default=PENDING
    )

    class Meta:
        """Meta class for Appointment model."""

        verbose_name = _("appointment")
        verbose_name_plural = _("appointments")
        ordering = ["created_at"]

    def __str__(self):
        """Return string representation of appointment."""
        return f"{self.user} - {self.purpose}"

    def save(self, *args, **kwargs):
        """Override save method."""
        self.end_appointment = self.start_appointment + timedelta(hours=1)
        super().save(*args, **kwargs)
