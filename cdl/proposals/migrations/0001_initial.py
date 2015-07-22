# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_proposals', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=680, blank=True)),
            ],
            options={
                'verbose_name': 'Capitole du Libre proposal category',
                'verbose_name_plural': 'Capitole du Libre proposal categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StandProposal',
            fields=[
                ('proposalbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='symposion_proposals.ProposalBase')),
                ('organisation', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'stand proposal',
            },
            bases=('symposion_proposals.proposalbase',),
        ),
        migrations.CreateModel(
            name='TalkProposal',
            fields=[
                ('proposalbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='symposion_proposals.ProposalBase')),
                ('audience_level', models.IntegerField(choices=[(1, 'Novice'), (3, 'Intermediate'), (2, 'Experienced')])),
                ('recording_release', models.BooleanField(default=True, help_text='By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box.')),
                ('duration', models.IntegerField(choices=[(0, 'No preference'), (1, 'I prefer a 20 minute slot'), (2, 'I prefer a 50 minute slot')])),
                ('category', models.ForeignKey(to='proposals.ProposalCategory')),
            ],
            options={
                'verbose_name': 'talk proposal',
            },
            bases=('symposion_proposals.proposalbase',),
        ),
        migrations.CreateModel(
            name='TutorialProposal',
            fields=[
                ('proposalbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='symposion_proposals.ProposalBase')),
                ('audience_level', models.IntegerField(choices=[(1, 'Novice'), (3, 'Intermediate'), (2, 'Experienced')])),
                ('recording_release', models.BooleanField(default=True, help_text='By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box.')),
                ('duration', models.IntegerField(choices=[(0, 'No preference'), (1, 'I prefer a 1h20 slot'), (2, 'I prefer a 2h50 slot')])),
                ('category', models.ForeignKey(to='proposals.ProposalCategory')),
            ],
            options={
                'verbose_name': 'tutorial proposal',
            },
            bases=('symposion_proposals.proposalbase',),
        ),
    ]
