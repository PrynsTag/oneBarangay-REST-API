# Generated by Django 4.0.2 on 2022-02-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_profile_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="created_at",
            field=models.DateTimeField(default=None),
        ),
    ]
