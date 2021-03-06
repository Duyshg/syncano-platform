# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-21 12:22
from django.db import migrations

import apps.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_acl'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=apps.core.fields.StrippedSlugField(max_length=64, null=True, default=None),
        ),
        migrations.AlterField(
            model_name='group',
            name='_is_live',
            field=apps.core.fields.LiveField(default=True),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set([('name', '_is_live')]),
        ),
    ]
