# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('difficulty_level', models.CharField(default=b'3', max_length=1)),
                ('company', models.ForeignKey(to='app1.Company', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=1024)),
                ('question', models.ForeignKey(to='app1.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('company', models.ForeignKey(to='app1.Company')),
            ],
        ),
        migrations.CreateModel(
            name='TestCandidateQuestionHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_dateTime', models.DateTimeField(null=True)),
                ('duration', models.SmallIntegerField(default=0)),
                ('status', models.SmallIntegerField(default=0)),
                ('score', models.SmallIntegerField(default=0)),
                ('answer', models.ForeignKey(to='app1.QuestionAnswer', null=True)),
                ('question', models.ForeignKey(to='app1.Question')),
            ],
        ),
        migrations.CreateModel(
            name='TestSectionDef',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('company', models.ForeignKey(to='app1.Company')),
            ],
        ),
        migrations.CreateModel(
            name='TestSectionQuestions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('duration', models.IntegerField(null=True, blank=True)),
                ('questions', models.ManyToManyField(to='app1.Question')),
                ('section', models.ForeignKey(to='app1.TestSectionDef')),
                ('test', models.ForeignKey(to='app1.Test')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('company', models.ForeignKey(to='app1.Company')),
            ],
        ),
        migrations.AddField(
            model_name='testcandidatequestionhistory',
            name='section',
            field=models.ForeignKey(to='app1.TestSectionDef'),
        ),
        migrations.AddField(
            model_name='testcandidatequestionhistory',
            name='test',
            field=models.ForeignKey(to='app1.Test'),
        ),
    ]
