# Generated by Django 2.1.5 on 2020-10-23 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0002_auto_20201022_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='title',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='day',
            name='graph',
        ),
        migrations.RemoveField(
            model_name='graph',
            name='description',
        ),
        migrations.RemoveField(
            model_name='graph',
            name='length',
        ),
        migrations.RemoveField(
            model_name='graph',
            name='timer',
        ),
        migrations.RemoveField(
            model_name='graph',
            name='title',
        ),
    ]