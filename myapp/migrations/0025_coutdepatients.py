# Generated by Django 4.2.3 on 2023-10-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_delete_coutdepatients'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoutDePatients',
            fields=[
                ('column', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('y2018', models.IntegerField()),
                ('y2019', models.IntegerField()),
                ('y2020', models.IntegerField()),
                ('y2021', models.IntegerField()),
            ],
        ),
    ]
