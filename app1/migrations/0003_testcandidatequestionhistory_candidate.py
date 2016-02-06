# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20150923_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcandidatequestionhistory',
            name='candidate',
            field=models.ForeignKey(default=True, to='app1.User'),
            preserve_default=False,
        ),
    ]
