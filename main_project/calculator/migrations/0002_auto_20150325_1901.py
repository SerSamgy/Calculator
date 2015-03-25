# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solver',
            name='cur_val',
        ),
        migrations.RemoveField(
            model_name='solver',
            name='res_val',
        ),
        migrations.RemoveField(
            model_name='solver',
            name='sign',
        ),
        migrations.AddField(
            model_name='solver',
            name='expression',
            field=models.CharField(default=b'0', max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='solver',
            name='result',
            field=models.CharField(default=b'0', max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
