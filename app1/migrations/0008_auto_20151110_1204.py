# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20151110_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to=b'static/app1/images/company/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(upload_to=b'static/app1/images/user/'),
        ),
    ]
