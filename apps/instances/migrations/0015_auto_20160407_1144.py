# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-07 11:44
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instances', '0014_instance_storage_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instanceindicator',
            name='type',
            field=models.SmallIntegerField(choices=[(0, 'schedules_count'), (1, 'storage_size'), (2, 'apns_devices')]),
        ),
    ]