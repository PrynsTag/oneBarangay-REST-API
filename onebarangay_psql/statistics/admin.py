"""Register your statistics models here."""
from adminactions import actions
from django.contrib import admin


actions.add_to_site(admin.site)
