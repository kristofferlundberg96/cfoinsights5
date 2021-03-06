# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_auto_20180128_2003'),
        ('speakers', '0003_auto_20180128_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='panel',
        ),
        migrations.AddField(
            model_name='speaker',
            name='panels',
            field=models.ManyToManyField(related_name='speakers', to='agenda.Panel'),
        ),
    ]
