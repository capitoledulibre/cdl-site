# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_conference', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=680, blank=True)),
                ('conference', models.ForeignKey(verbose_name='conference', to='symposion_conference.Conference')),
            ],
            options={
                'verbose_name': 'Conference category',
                'verbose_name_plural': 'Th\xe9matiques',
            },
            bases=(models.Model,),
        ),
    ]
