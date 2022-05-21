from django.db import models
from django.db import models
# from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

class Event(models.Model):
  title = models.CharField(max_length=64)
  description = models.CharField(max_length=600)
  date = models.DateField()
  likes = models.IntegerField()
  category = models.CharField(max_length=64)

  def __str__(self):
    return self.title

class Comment(models.Model):
  words = models.CharField(max_length=600)
  event_posted_on = models.ForeignKey(Event, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'comment on {self.event_posted_on} by {self.user.username}'

class UserTimeline(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  year = models.IntegerField()
  categories = models.CharField(max_length=60)

  def __str__(self):
    return f"{self.user.username}'s timeline"