from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
   # organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
       return self.title
class User(User):
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.username
