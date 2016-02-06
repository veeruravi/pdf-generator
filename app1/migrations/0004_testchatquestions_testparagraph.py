# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_testcandidatequestionhistory_candidate'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestChatQuestions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('transcripts', models.TextField()),
                ('question', models.ForeignKey(to='app1.Question')),
            ],
        ),
        migrations.CreateModel(
            name='TestParagraph',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('paragraph', models.TextField()),
                ('question', models.ForeignKey(to='app1.Question')),
            ],
        ),
    ]
