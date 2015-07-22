# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkproposal',
            name='prerequistes',
            field=models.TextField(help_text='If Prerequistes are needed to follow this talk or workshop.', verbose_name='Prerequistes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talkproposal',
            name='technical_information',
            field=models.TextField(help_text="Specify definition screen, computer output, if you need a computer. Won't be public.", verbose_name='Technical information', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tutorialproposal',
            name='prerequistes',
            field=models.TextField(help_text='If Prerequistes are needed to follow this talk or workshop.', verbose_name='Prerequistes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tutorialproposal',
            name='technical_information',
            field=models.TextField(help_text="Specify definition screen, computer output, if you need a computer. Won't be public.", verbose_name='Technical information', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='talkproposal',
            name='audience_level',
            field=models.IntegerField(verbose_name='Audience level', choices=[(1, 'Novice'), (3, 'Intermediate'), (2, 'Experienced')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='talkproposal',
            name='duration',
            field=models.IntegerField(verbose_name='Duration', choices=[(0, 'No preference'), (1, 'I prefer a 20 minute slot'), (2, 'I prefer a 50 minute slot')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='audience_level',
            field=models.IntegerField(verbose_name='Audience level', choices=[(1, 'Novice'), (3, 'Intermediate'), (2, 'Experienced')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='duration',
            field=models.IntegerField(verbose_name='Duration', choices=[(0, 'No preference'), (1, 'I prefer a 1h20 slot'), (2, 'I prefer a 2h50 slot')]),
            preserve_default=True,
        ),
    ]
