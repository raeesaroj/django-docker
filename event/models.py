from django.db import models
from bipad.models import TimeStampedModal


class Event(TimeStampedModal):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title
