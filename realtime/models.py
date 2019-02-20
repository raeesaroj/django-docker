from django.contrib.gis.db import models
from bipad.models import TimeStampedModal


class Earthquake(TimeStampedModal):
    description = models.TextField(default=None, null=True, blank=True)
    point = models.PointField()
    magnitude = models.FloatField()
    address = models.CharField(max_length=255, null=True, blank=True)
    event_on = models.DateTimeField()
