"""Register your rbi models here."""
from django.contrib import admin

from onebarangay_psql.rbi import models

admin.site.register(models.HouseRecord)
admin.site.register(models.FamilyMember)
