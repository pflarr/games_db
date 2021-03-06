from django.conf.urls import patterns, url

from games_app import views

urlpatterns = patterns('',
    url(r'^$', views.games_list, name='games_latest', kwargs={'ev':None}),
    url(r'^(?P<ev>\d+)/$', views.games_list, name='games'),

    url(r'^req/(?P<ev>\d+)/$', views.games_req, name='games_req'),
    url(r'^req/(?P<ev>\d+)/d/$', views.games_req, name='games_req_delete'),
    url(r'^req/(?P<ev>\d+)/u/$', views.games_req, name='games_req_update'),

    url(r'^events/$', views.event_list, name='events'),
    url(r'^events/c/$', views.CreateEvent.as_view(), name='event_create'),
    url(r'^events/u(?P<pk>\d+)/$', views.UpdateEvent.as_view(), name='event_update'),
    url(r'^events/d/(?P<pk>\d+)/$', views.DeleteEvent.as_view(), name='event_delete'),
)
