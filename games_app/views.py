from django.http import HttpResponse
from django.template import RequestContext, loader

from games_tracker.models import GamesTB, Event, Comments 

def games_list(request):
    games_list = GamesTB.objects.order_by('added')
    events = GamesTB.objects.order_by('added')
    template = loader.get_template('games_tracker/games_list.html')
    context = RequestContext(request, {
        'games_list': games_list,
        'events': events,
    })
    return HttpResponse(template.render(context))

def game_request(request):
  
