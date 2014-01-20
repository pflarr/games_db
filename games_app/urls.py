from django.conf.urls import patterns, url

from games_tracker import views

urlpatterns = patterns('',
    url(r'^$', views.games_list, name='games_list'),
    url(r'^game_request/$', views.game_request, name='game_request')
)
