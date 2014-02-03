from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic.edit import FormView, ModelFormMixin
from django_tables2 import RequestConfig, SingleTableMixin

from games_app.models import Game, Event
from games_app.tables import EventTable
from games_app.forms import EventForm

def index(request, ev):
    event = get_object_or_404(Event, pk=ev)
    games_list = Game.objects.order_by('added')
    events = Event.objects.order_by('added')
    template = loader.get_template('games_app/index.dhtml')
    context = RequestContext(request, {
        'games_list': games_list,
        'events': events,
        'event': event,
    })
    return HttpResponse(template.render(context))

'''class EventList(ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'games_app/events.dhtml'
'''
def event_list(request):
    table = EventTable(Event.objects.all())
    table.paginate(page=request.GET.get('page',1), per_page=2)
    RequestConfig(request, paginate={'per_page':2}).configure(table)

    event_form = EventForm()

    return render(request, 'games_app/events.dhtml', {'events':table,
                                                      'form':event_form}) 
class EditEvents(FormView, SingleTableMixin, ModelFormMixin):
    table_class = EventTable
    context_table_name = 'events'
    table_pagination = {'per_page':2}
    template_name='games_app/events.dhtml'
    form_class = EventForm
    model = Event
    success_url = '/games/events/'

def add_req(request, ev):
    event = get_object_or_404(Event, pk=event_id)

    return HTTPResponseRedirect(reverse('games_app:index', args=(event,)))
