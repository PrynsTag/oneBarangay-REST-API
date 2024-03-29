"""Create forms for the user's app."""
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms, get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    """Form for User change password."""

    class Meta(admin_forms.UserChangeForm.Meta):
        """Meta class for UserAdminChangeForm."""

        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """Form for User Creation in the Admin Area.

    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        """Meta class for UserAdminCreationForm."""

        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """Form that will be rendered on a user sign up section/screen.

    Default fields will be added automatically. Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """Renders the form when user has signed up using social accounts.

    Default fields will be added automatically. See UserSignupForm otherwise.
    """
