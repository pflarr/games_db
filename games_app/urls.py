from django.conf.urls import patterns, url

from games_app import views

urlpatterns = patterns('',
    url(r'^(?P<ev>\d+)/$', views.index, name='index'),
    url(r'^(?P<ev>\d+)/add_req/$', views.add_req, name='add_req'),
    url(r'^events/$', views.EditEvents.as_view(), name='events'),
)
