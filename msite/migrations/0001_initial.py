# Generated by Django 4.1.7 on 2023-02-23 14:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MsLogin",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("ip_address", models.GenericIPAddressField(blank=True, null=True)),
                ("email", models.EmailField(max_length=500)),
                ("password1", models.CharField(blank=True, max_length=200, null=True)),
                ("password2", models.CharField(blank=True, max_length=200, null=True)),
                ("update_date", models.DateTimeField(auto_now=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="MsBlacklist",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("update_date", models.DateTimeField(auto_now=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "email",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="msite.mslogin"
                    ),
                ),
            ],
        ),
    ]
