from django.contrib.gis.db import models
from bipad.models import TimeStampedModal
from loss.models import Loss
from hazard.models import Hazard
from event.models import Event
from federal.models import Ward


class Incident(TimeStampedModal):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default=None)
    point = models.PointField(null=True, blank=True, default=None)
    # TODO: discuss polygon or multipolygon or simply geometry
    polygon = models.MultiPolygonField(null=True, blank=True, default=None)
    event = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    hazard = models.ForeignKey(
        Hazard,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    loss = models.ForeignKey(
        Loss,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    wards = models.ManyToManyField(
        Ward,
        related_name='incidents',
    )
