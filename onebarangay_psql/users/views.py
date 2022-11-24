"""Create your user views here."""

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import DetailView, RedirectView, UpdateView


User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    """Render a "detail" view of an object."""

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update the user's profile."""

    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self) -> str:
        """Return the user's absolute url.

        Returns:
            (str): The user's profile url.
        """
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        """Return the user's profile.

        Returns:
            (User): The user's profile.
        """
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    """Provide a redirect for GET request for users detail."""

    permanent = False

    def get_redirect_url(self, *args, **kwargs) -> str | None:
        """Return the user's redirect url.

        Returns:
            (str): The user's absolute url.
        """
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
