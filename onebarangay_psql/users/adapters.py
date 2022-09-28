"""Create your Adapters for user's app."""
from typing import Any

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.http import HttpRequest


class AccountAdapter(DefaultAccountAdapter):
    """AccountAdapter class."""

    @staticmethod
    def is_open_for_signup(request: HttpRequest) -> bool:
        """Check whether the site is open for signups.

        Args:
            request (HttpRequest): The request object.

        Returns:
            bool: True if the site is open for signups, False otherwise.
        """
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    """SocialAccountAdapter class."""

    @staticmethod
    def is_open_for_signup(request: HttpRequest, sociallogin: Any) -> bool:
        """Check if social account is open for signup.

        Args:
            request (HttpRequest): Django request object.
            sociallogin (Any): SocialLogin object.

        Returns:
            bool: True if social account is open for signup, False otherwise.
        """
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
