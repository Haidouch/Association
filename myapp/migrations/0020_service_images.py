# Generated by Django 4.2.3 on 2023-09-29 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='images',
            field=models.ImageField(default=1, upload_to='service/'),
            preserve_default=False,
        ),
    ]
