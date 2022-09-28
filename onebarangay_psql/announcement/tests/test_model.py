"""Create your announcement model tests here."""
import pytest

from onebarangay_psql.announcement.models import Announcement
from onebarangay_psql.users.models import User

pytestmark = pytest.mark.django_db


class TestAnnouncement:
    """Test the Announcement model."""

    @staticmethod
    def test_create_announcement(admin_user: User) -> None:
        """Test creating an announcement.

        Args:
            admin_user (User): The admin user creating the announcement.
        """
        a1 = Announcement.objects.create(
            title="Test Announcement",
            content="This is a test announcement.",
            author=admin_user,
            tags="this is a test announcement",
        )

        assert a1.title == "Test Announcement"
        assert a1.slug == "test-announcement"
        assert a1.content == "This is a test announcement."
        assert a1.author == admin_user
        assert a1.tags == "this is a test announcement"

    @staticmethod
    def test_str(admin_user: User) -> None:
        """Test the string representation of an announcement.

        Args:
            admin_user (User): The admin user creating the announcement.
        """
        a1 = Announcement.objects.create(
            title="Test Announcement",
            content="This is a test announcement.",
            author=admin_user,
            tags="this is a test announcement",
        )

        assert str(a1) == "Test Announcement"

    @staticmethod
    def test_get_absolute_url(admin_user: User) -> None:
        """Test the absolute url of an announcement.

        Args:
            admin_user (User): The admin user creating the announcement.
        """
        a1 = Announcement.objects.create(
            title="Test Announcement",
            content="This is a test announcement.",
            author=admin_user,
            tags="this is a test announcement",
        )

        assert a1.get_absolute_url() == f"/api/announcement/{a1.slug}/"

    @staticmethod
    def test_save_announcement(admin_user: User) -> None:
        """Test saving an announcement.

        Args:
            admin_user (User): The admin user creating the announcement.
        """
        a1 = Announcement.objects.create(
            title="Test Announcement",
            content="This is a test announcement.",
            author=admin_user,
            tags="this is a test announcement",
        )

        a1.title = "Updated Test Announcement"
        a1.save()

        assert a1.title == "Updated Test Announcement"

    @staticmethod
    def test_announcement_ordering(admin_user: User) -> None:
        """Test the ordering of announcements.

        The most recent announcement should be first.
        Args:
            admin_user (User): The admin user creating the announcement.
        """
        a1 = Announcement.objects.create(
            title="Test Announcement",
            content="This is a test announcement.",
            author=admin_user,
            tags="this is a test announcement",
        )

        a2 = Announcement.objects.create(
            title="Test Announcement 2",
            content="This is a test announcement.",
            author=admin_user,
            tags="this is a test announcement",
        )
        announcements = Announcement.objects.all()
        assert a1.title == "Test Announcement"
        assert a2.title == "Test Announcement 2"
        assert announcements[0].title == "Test Announcement 2"
        assert announcements[1].title == "Test Announcement"
