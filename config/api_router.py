"""Create your user API router here."""
from django.conf import settings
from rest_framework.routers import BaseRouter, DefaultRouter, SimpleRouter

from onebarangay_psql.announcement.viewset import AnnouncementViewSet
from onebarangay_psql.appointment.viewset import AppointmentViewSet, StatusUpdateViewSet
from onebarangay_psql.rbi.viewset import FamilyMemberViewSet, HouseRecordViewSet
from onebarangay_psql.statistics import viewset
from onebarangay_psql.users.api.views import (
    ProfilePhotoViewSet,
    ProfileViewSet,
    UserViewSet,
)

router = BaseRouter()

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("user", UserViewSet)
router.register("profile", ProfileViewSet)
router.register("profile/change_photo", ProfilePhotoViewSet, "change_photo")
router.register("announcement", AnnouncementViewSet)
router.register("appointment", AppointmentViewSet)
router.register("status", StatusUpdateViewSet, basename="status")
router.register("house-record", HouseRecordViewSet, basename="house")
router.register("family-member", FamilyMemberViewSet, basename="family")
router.register(
    "statistics/user-signup",
    viewset.UserSignUpMaterializedViewSet,
    basename="mv-signup",
)
router.register(
    "statistics/totals", viewset.TotalMaterializedViewSet, basename="mv-total"
)
router.register(
    "statistics/appointment",
    viewset.AppointmentMaterializedViewSet,
    basename="mv-appointment",
)
router.register(
    "statistics/user-login", viewset.UserLogInMaterializedViewSet, basename="mv-signin"
)
router.register(
    "statistics/age-group", viewset.AgeGroupMaterializedViewSet, basename="mv-age-group"
)
router.register(
    "statistics/citizenship",
    viewset.CitizenshipMaterializedViewSet,
    basename="mv-citizenship",
)
router.register(
    "statistics/civil-status",
    viewset.CivilStatusMaterializedViewSet,
    basename="mv-civil-status",
)
router.register(
    "statistics/average", viewset.AverageMaterializedViewSet, basename="mv-average"
)
router.register(
    "statistics/social-class",
    viewset.SocialClassMaterializedViewSet,
    basename="mv-social-class",
)
router.register(
    "statistics/user-login-by-month",
    viewset.UserLoginMonthlyMaterializedViewSet,
    basename="mv-login-monthly",
)
router.register(
    "statistics/user-signup-by-month",
    viewset.UserSignUpMonthlyMaterializedViewSet,
    basename="mv-signup-monthly",
)
router.register(
    "statistics/refresh",
    viewset.RefreshMaterialViewSet,
    basename="mv-refresh",
)

app_name = "api"
urlpatterns = router.urls
