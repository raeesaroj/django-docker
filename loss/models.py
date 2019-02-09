from django.db import models
from django.contrib.postgres.fields import JSONField
from bipad.models import TimeStampedModal


class Loss(TimeStampedModal):
    description = models.TextField(null=True, blank=True, default=None)
    deaths = models.IntegerField(null=True, blank=True, default=None)
    injured = models.IntegerField(null=True, blank=True, default=None)
    missing = models.IntegerField(null=True, blank=True, default=None)
    house_destroyed = models.IntegerField(null=True, blank=True, default=None)
    house_affected = models.IntegerField(null=True, blank=True, default=None)
    indirectly_affected = models.IntegerField(null=True, blank=True, default=None)
    directly_affected = models.IntegerField(null=True, blank=True, default=None)
    relocated = models.IntegerField(null=True, blank=True, default=None)
    evacuated = models.IntegerField(null=True, blank=True, default=None)
    loss_nrs = models.IntegerField(null=True, blank=True, default=None)
    educational_centers_affected = models.IntegerField(null=True, blank=True, default=None)
    hospital_affected = models.IntegerField(null=True, blank=True, default=None)
    livestock_destroyed = models.IntegerField(null=True, blank=True, default=None)
    road_damaged = models.IntegerField(null=True, blank=True, default=None)
    meta = JSONField(null=True, blank=True, default=None)
