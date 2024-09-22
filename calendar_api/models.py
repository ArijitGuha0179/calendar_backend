from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    # Link each event to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Event details
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # Optional description
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        # String representation of the event
        return self.title
