# Generated by Django 2.1.5 on 2020-10-10 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_ajax', '0003_task2_timer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task2',
            name='timer',
            field=models.BigIntegerField(default=0),
        ),
    ]
