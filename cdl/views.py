
import datetime

from django.http import HttpResponse
from django.utils.html import escape
from django.utils.text import slugify
from symposion.schedule.models import Room, Presentation


def schedule_xml(request):

    result = """<?xml version="1.0" encoding="UTF-8"?>
<schedule>
  <conference>
    <title>Capitole du Libre 2015</title>
    <subtitle/>
    <venue>ENSEEIHT (26 rue Riquet, Toulouse)</venue>
    <city>Toulouse</city>
    <start>2015-11-21</start>
    <end>2015-11-22</end>
    <days>2</days>
    <day_change>09:00:00</day_change>
    <timeslot_duration>00:05:00</timeslot_duration>
  </conference>
"""

    days = [datetime.date(2015, 11, 21), datetime.date(2015, 11, 22)]
    for index, day in enumerate(days):
        result += '  <day index="%s" date="%s">\n' % (index, day)
        for room in Room.objects.all():
            result += '    <room name="%s">\n' % room
            for p in Presentation.objects.filter(slot__day__date=day, slot__slotroom__room=room).distinct():
                start_at = datetime.datetime.combine(day, p.slot.start)
                end_at = datetime.datetime.combine(day, p.slot.end)
                duration = end_at - start_at
                result += """      <event id="%(id)s">
        <start>%(start)s</start>
        <duration>%(duration)s</duration>
        <room>%(room)s</room>
        <slug>%(slug)s</slug>
        <title>%(title)s</title>
        <subtitle/>
        <track>%(track)s</track>
        <type>%(type)s</type>
        <language/>
        <abstract>%(abstract)s</abstract>
        <description>%(description)s</description>
        <persons>
          <person id="%(person_id)s">%(person)s</person>
        </persons>
        <links>
        </links>
      </event>\n""" % {
                    'id': p.id,
                    'start': p.slot.start.strftime('%H:%M'),
                    'duration': '%02d:%02d' % (duration.total_seconds() / 3600, duration.total_seconds() % 3600 / 60),
                    'room': room,
                    'slug': slugify(p.title),
                    'title': escape(p.title),
                    'track': p.proposal.category,
                    'type': p.proposal.kind,
                    'abstract': escape(p.description),
                    'description': escape(p.abstract),
                    'person_id': p.speaker.id,
                    'person': p.speaker,
                }
                # print p.id
                # print p.slot.start
                # print p.slot.end
                # print room
                # print p.title
                # print p.title
                # print p.proposal.category
                # print p.proposal.kind
                # print p.abstract
                # print p.speaker
                # print "*****************"
            result += "    </room>\n"
        result += "  </day>\n"
    result += "</schedule>\n"
    result = result.replace('&','&amp;')
    return HttpResponse(result, content_type="application/xml")

