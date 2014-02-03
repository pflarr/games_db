from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=30, verbose_name='Event')
    added = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return '<Event: %s>' % self.name

class Game(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=50)
    bringer = models.CharField(max_length=20)
    requester = models.CharField(max_length=20, null=True)
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "<Game: %s, %s>" % (self.game, self.bringer)

    class Meta:
        unique_together = (('name','event'),)
   
class Comment(models.Model):
    game = models.ForeignKey(Game)
    comm_txt = models.CharField(max_length=80)

    def __unicode__(self):
        return "<GameComment: %s, %s>" % (self.ame, self.comm_txt)

class Player(models.Model):
    game = models.ForeignKey(Game)
    event = models.ForeignKey(Event)
    who = models.CharField(max_length=20) 
    
