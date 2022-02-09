"""Register your announcement models here."""
from django.contrib import admin

from onebarangay_psql.announcement.models import Announcement

admin.site.register(Announcement)
