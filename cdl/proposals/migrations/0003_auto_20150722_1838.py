# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0002_auto_20150722_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talkproposal',
            name='technical_information',
        ),
        migrations.RemoveField(
            model_name='tutorialproposal',
            name='technical_information',
        ),
        migrations.AddField(
            model_name='talkproposal',
            name='broadcast_audio',
            field=models.BooleanField(default=None, help_text='Do you need audio material to broadcast audio ?', verbose_name='Broadcast audio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talkproposal',
            name='video_output',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, help_text='Specify video output.', max_length=25, verbose_name='Video output', choices=[(b'VGA', 'VGA'), (b'DVI', 'DVI'), (b'HDMI', 'HDMI'), (b'DPORT', 'Display Port'), (b'MDPORT', ' Mini Display Port')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tutorialproposal',
            name='broadcast_audio',
            field=models.BooleanField(default=None, help_text='Do you need audio material to broadcast audio ?', verbose_name='Broadcast audio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tutorialproposal',
            name='video_output',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, help_text='Specify video output.', max_length=25, verbose_name='Video output', choices=[(b'VGA', 'VGA'), (b'DVI', 'DVI'), (b'HDMI', 'HDMI'), (b'DPORT', 'Display Port'), (b'MDPORT', ' Mini Display Port')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='talkproposal',
            name='recording_release',
            field=models.BooleanField(default=True, help_text='By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box.', verbose_name='Recording release'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='recording_release',
            field=models.BooleanField(default=True, help_text='By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box.', verbose_name='Recording release'),
            preserve_default=True,
        ),
    ]
