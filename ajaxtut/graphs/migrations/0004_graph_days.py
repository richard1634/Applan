# Generated by Django 2.1.5 on 2020-10-23 22:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0003_auto_20201023_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='days',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), default=list, size=None),
        ),
    ]
