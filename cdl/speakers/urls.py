from django.conf.urls import patterns, url


urlpatterns = patterns("cdl.speakers.views",
    url(r"^edit/(?:(?P<pk>\d+)/)?$", "speaker_edit_staff", name="speaker_edit_staff"),
)
