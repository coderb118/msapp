# Generated by Django 4.0.6 on 2023-03-03 12:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('msite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msworks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]