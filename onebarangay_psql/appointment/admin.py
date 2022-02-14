"""Register your appointment models here."""
from django.contrib import admin

from onebarangay_psql.appointment.models import Appointment

admin.site.register(Appointment)
