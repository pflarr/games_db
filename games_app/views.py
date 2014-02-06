from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_tables2 import RequestConfig, SingleTableMixin

from games_app.models import Game, Event
from games_app.tables import EventTable, RequestedGamesTable
from games_app.tables import ConfirmedGamesTable
from games_app.forms import EventForm

def games_list(request, ev=None):
    if ev is not None:
        event = get_object_or_404(Event, pk=ev)
    else:
        event = Event.objects.order_by('added')[0]
    games = Game.objects.all().filter(event__exact=event)
    games_requested = games.filter(bringer__exact='')
    games_confirmed = games.exclude(bringer__exact='')
    template = 'games_app/games.dhtml'
    req_table = RequestedGamesTable(games_requested, prefix="req-")
    conf_table = ConfirmedGamesTable(games_confirmed, prefix="conf-")
    RequestConfig(request).configure(req_table)
    RequestConfig(request).configure(conf_table)
   
    return render(request, template, {'req_table': req_table,
                                      'conf_table': conf_table})

def event_list(request):
    table = EventTable(Event.objects.all())
    table.paginate(page=request.GET.get('page',1), per_page=6)
    RequestConfig(request, paginate={'per_page':6}).configure(table)

    event_form = EventForm()

    return render(request, 'games_app/events.dhtml', {'events':table,
                                                      'form':event_form}) 

class CreateEvent(CreateView):
    model = Event
    success_url = reverse_lazy('events')

class UpdateEvent(UpdateView):
    model = Event
    success_url = reverse_lazy('events')
    template_name = "games_app/event_edit.dhtml"

class DeleteEvent(DeleteView):
    model = Event
    success_url = reverse_lazy('events')
    template_name = "games_app/event_confirm_delete.dhtml"

