# Generated by Django 2.1.5 on 2020-10-10 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_ajax', '0005_auto_20201010_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task2',
            name='timer',
        ),
    ]
