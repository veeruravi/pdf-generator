# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_testchatquestions_testparagraph'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestChatTranscripts',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('transcripts', models.TextField()),
                ('question', models.ForeignKey(to='app1.Question')),
            ],
        ),
        migrations.RemoveField(
            model_name='testchatquestions',
            name='question',
        ),
        migrations.DeleteModel(
            name='TestChatQuestions',
        ),
    ]
