from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from dhango.urlresolvers import reverse

from games_app.models import GameTB, Event

def games_list(request, ev):
    event = get_object_or_404(Event, pk=ev)
    games_list = Game.objects.order_by('added')
    events = Event.objects.order_by('added')
    template = loader.get_template('games_app/index.html')
    context = RequestContext(request, {
        'games_list': games_list,
        'events': events,
    })
    return HttpResponse(template.render(context))

def game_request(request, ev):
    event = get_object_or_404(Event, pk=event_id)

    return HTTPResponseRedirect(reverse('games_app:index', args=(ev=event,)))
