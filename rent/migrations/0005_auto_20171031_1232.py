# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-31 04:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_auto_20171031_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='hourse_tel',
            new_name='house_tel',
        ),
    ]
