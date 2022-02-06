"""Utility for storing static files in Google Cloud Storage."""
from storages.backends.gcloud import GoogleCloudStorage


class StaticRootGoogleCloudStorage(GoogleCloudStorage):
    """Static root storage class for Google Cloud Storage."""

    location = "static"
    default_acl = "publicRead"


class MediaRootGoogleCloudStorage(GoogleCloudStorage):
    """Media root storage class for Google Cloud Storage."""

    location = "media"
    file_overwrite = False
