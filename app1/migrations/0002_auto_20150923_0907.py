# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(default=False, upload_to=b'images/company/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(default=False, upload_to=b'images/company/'),
            preserve_default=False,
        ),
    ]
