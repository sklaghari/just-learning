# Generated by Django 3.2 on 2021-05-07 07:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('feeds', '0002_notification'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='Notification1',
        ),
    ]
