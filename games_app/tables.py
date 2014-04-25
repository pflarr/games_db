import django_tables2 as tables
from django_tables2.utils import A
from games_app.models import Event, Game, Comment, Player
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.safestring import mark_safe


class RequestedGamesTable(tables.Table):
    event = tables.Column(visible=False)
    bringer = tables.Column(visible=False)

    class Meta:
        attrs = {"class": "paleblue"}
        model = Game


class ConfirmedGamesTable(tables.Table):
    event = tables.Column(visible=False)

    class Meta:
        attrs = {"class": "paleblue"}
        model = Game


class EventTable(tables.Table):
    class Meta:
        attrs = {"class": "paleblue"}
        model = Event
        sequence = ("name", "added", 'id')

    name = tables.LinkColumn('games', kwargs={'ev':A('pk')})
    id = tables.Column(sortable=False, verbose_name="Actions")
                
    def render_id(self, record):
        if record.game_set.exists():
            return mark_safe('<a href="%s">Edit</a>' % reverse('event_update',
                                                               kwargs={'pk': record.id}))
        else:
            return mark_safe('<a href="%s">Delete</a>' % reverse('event_delete',
                                                                 kwargs={'pk': record.id}))
