"""Create your user API router here."""
from django.conf import settings
from rest_framework.routers import BaseRouter, DefaultRouter, SimpleRouter

from onebarangay_psql.users.api.views import (
    UserListViewSet,
    UserProfileListViewSet,
    UserProfileViewSet,
    UserViewSet,
)

router = BaseRouter()

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("user", UserViewSet)
router.register("list-users", UserListViewSet)
router.register("profile", UserProfileViewSet)
router.register("list-profiles", UserProfileListViewSet)

app_name = "api"
urlpatterns = router.urls
