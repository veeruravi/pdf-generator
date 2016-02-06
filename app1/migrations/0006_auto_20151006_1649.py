# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20151006_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='testchattranscripts',
            name='candidate',
            field=models.ForeignKey(default=0, to='app1.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testchattranscripts',
            name='question',
            field=models.TextField(),
        ),
    ]
