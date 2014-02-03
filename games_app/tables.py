import django_tables2 as tables
from games_app.models import Event

class EventTable(tables.Table):
    name = tables.Column()
    id = tables.Column(visible=False)
    class Meta:
        attrs = {"class": "paleblue"}
        model = Event
        sequence = ("name", "added")
                

