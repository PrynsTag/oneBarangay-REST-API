"""Create your announcement drf http methods tests here."""
from django.contrib.auth import get_user_model
from django.test.client import Client
from django.urls import reverse
from rest_framework import status

from onebarangay_psql.announcement.models import Announcement

User = get_user_model()


class TestAnnouncementViewSetUrls:
    """Test AnnouncementViewSet URLs."""

    @staticmethod
    def test_announcement_list_url(admin_api_client: Client) -> None:
        """Test the announcement list url.

        Args:
            admin_api_client (Client): The admin api client.
        """
        response = admin_api_client.get(reverse("api:announcement-list"))
        assert response.status_code == status.HTTP_200_OK

    @staticmethod
    def test_announcement_retrieve_url(
        admin_api_client: Client, announcement: Announcement
    ) -> None:
        """Test the announcement retrieve url.

        Args:
            admin_api_client (Client): The admin api client.
            announcement (Announcement): The announcement to be retrieved.
        """
        response = admin_api_client.get(
            reverse("api:announcement-detail", kwargs={"slug": announcement.slug})
        )

        assert response.status_code == status.HTTP_200_OK

    @staticmethod
    def test_announcement_create_url(admin_api_client: Client) -> None:
        """Test the announcement create url.

        Args:
            admin_api_client (Client): The admin api client.
        """
        response = admin_api_client.post(
            reverse("api:announcement-list"),
            {
                "title": "This is a new announcement",
                "content": "This is the content of the new announcement",
                "is_featured": "True",
                "tags": '["tag1", "tag2"]',
            },
        )
        assert response.status_code == status.HTTP_201_CREATED

    @staticmethod
    def test_announcement_update_url(
        admin_api_client: Client, announcement: Announcement
    ) -> None:
        """Test the announcement update url.

        Args:
            admin_api_client (Client): The admin api client.
            announcement (Announcement): The announcement to be updated.
        """
        response = admin_api_client.put(
            reverse("api:announcement-detail", kwargs={"slug": announcement.slug}),
            {
                "title": announcement.title + " updated",
                "content": announcement.content,
                "is_featured": announcement.is_featured,
                "tags": '["tag1", "tag2"]',
            },
        )
        assert response.status_code == status.HTTP_200_OK

    @staticmethod
    def test_announcement_partial_update_url(
        admin_api_client: Client, announcement: Announcement
    ) -> None:
        """Test the announcement partial update url.

        Args:
            admin_api_client (Client): The admin api client.
            announcement (Announcement): The announcement to be updated.
        """
        response = admin_api_client.patch(
            reverse("api:announcement-detail", kwargs={"slug": announcement.slug}),
            {
                "content": announcement.content + " updated",
            },
        )
        assert response.status_code == status.HTTP_200_OK

    @staticmethod
    def test_announcement_delete_url(
        admin_api_client: Client, announcement: Announcement
    ) -> None:
        """Test the announcement delete url.

        Args:
            admin_api_client (Client): The admin api client.
            announcement (Announcement): The announcement to be deleted.
        """
        response = admin_api_client.delete(
            reverse("api:announcement-detail", kwargs={"slug": announcement.slug})
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
