from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^(?P<route_slug>[\w\-]+)/$', 'graphs.views.graphs', name="graphs"),
)
