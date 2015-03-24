# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cur_val', models.IntegerField(default=0)),
                ('res_val', models.IntegerField(default=0)),
                ('sign', models.CharField(default=None, max_length=1, blank=True)),
                ('result', models.CharField(default=b'0', max_length=10, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
