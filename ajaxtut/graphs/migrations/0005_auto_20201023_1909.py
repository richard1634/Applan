# Generated by Django 2.1.5 on 2020-10-24 02:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0004_graph_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='numbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='graph',
            name='days',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), blank=True, default=list, size=None),
        ),
    ]
