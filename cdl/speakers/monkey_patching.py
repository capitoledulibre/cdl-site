# -*- coding: utf-8 -*-
# monkey_patching Speaker add organisation field

from django.db import models
from symposion.speakers.models import Speaker

Speaker.add_to_class('organisation', models.CharField(max_length=100,blank=True))
Speaker.add_to_class('city', models.CharField(max_length=255,blank=True))
Speaker.add_to_class('need_travel', models.BooleanField(default=False))
Speaker.add_to_class('need_hosting', models.BooleanField(default=False))
