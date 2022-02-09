"""Create your announcement models here."""
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

user = get_user_model()


class Announcement(models.Model):
    """Announcement model."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(_("title"), max_length=255, unique=True)
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, auto_created=True)
    content = models.TextField(_("content"))
    is_featured = models.BooleanField(default=False)
    thumbnail = models.ImageField(
        upload_to="announcement/thumbnail", default="announcement/thumbnail/default.jpg"
    )
    tags = TaggableManager(_("tags"))
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

    def get_absolute_url(self):
        """Return the url to access a particular announcement instance."""
        return reverse("api:announcement-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """Override the save method to create a slug and username from the models.

        Args:
            *args (list): list of arguments
            **kwargs (dict): dictionary of keyword arguments
        """
        if not self.slug:
            self.slug = slugify(self.title)

        self.username = self.author.username
        super().save(*args, **kwargs)

    class Meta:
        """Metaclass for Announcement model."""

        ordering = ["-created_at"]
