# Generated by Django 4.2.3 on 2023-09-29 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_service_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitie',
            old_name='description',
            new_name='href',
        ),
    ]
