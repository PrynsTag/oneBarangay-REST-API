# Generated by Django 4.0.2 on 2022-02-09 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("announcement", "0005_announcement_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="announcement",
            name="username",
            field=models.CharField(auto_created=True, default="prince", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="announcement",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
