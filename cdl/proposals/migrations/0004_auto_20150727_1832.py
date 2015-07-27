# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0003_auto_20150722_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talkproposal',
            name='category',
            field=models.ForeignKey(to='conference.ConferenceCategory'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='category',
            field=models.ForeignKey(to='conference.ConferenceCategory'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='ProposalCategory',
        ),
    ]
