# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-23 10:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_panel_roundtable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panel',
            name='roundtable',
        ),
    ]
