# Generated by Django 4.2.3 on 2023-08-28 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_depenses_revenus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depenses',
            name='valeur',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='revenus',
            name='valeur',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
