from django.db import models
from django.contrib.postgres.fields import JSONField
from bipad.models import TimeStampedModal


class Loss(TimeStampedModal):
    description = models.TextField(null=True, blank=True, default=None)
    deaths = models.PositiveIntegerField(null=True, blank=True, default=None)
    injured = models.PositiveIntegerField(null=True, blank=True, default=None)
    missing = models.PositiveIntegerField(null=True, blank=True, default=None)
    relocated = models.PositiveIntegerField(null=True, blank=True, default=None)
    evacuated = models.PositiveIntegerField(null=True, blank=True, default=None)

    indirectly_affected = models.PositiveIntegerField(null=True, blank=True, default=None)
    directly_affected = models.PositiveIntegerField(null=True, blank=True, default=None)

    house_destroyed = models.PositiveIntegerField(null=True, blank=True, default=None)
    house_affected = models.PositiveIntegerField(null=True, blank=True, default=None)
    educational_centers_affected = models.PositiveIntegerField(null=True, blank=True, default=None)
    hospital_affected = models.PositiveIntegerField(null=True, blank=True, default=None)
    livestock_destroyed = models.PositiveIntegerField(null=True, blank=True, default=None)
    road_damaged = models.PositiveIntegerField(null=True, blank=True, default=None)
    loss_nrs = models.PositiveIntegerField(null=True, blank=True, default=None)
    detail = JSONField(null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = "losses"


class People(models.Model):
    DEAD = 'dead'
    MISSING = 'missing'
    INJURED = 'injured'
    AFFECTED = 'affected'

    STATUS = (
        (DEAD, 'Dead'),
        (MISSING, 'Missing'),
        (INJURED, 'Injured'),
        (AFFECTED, 'Affected'),
    )

    status = models.CharField(max_length=25, choices=STATUS)
    name = models.CharField(max_length=255, null=True, blank=True, default=None)
    age = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    below_poverty = models.BooleanField(null=True, blank=True, default=None)
    disabled = models.BooleanField(null=True, blank=True, default=None)


class InfrastructureType(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, default=None)


class Infrastructure(models.Model):
    DESTROYED = 'destroyed'
    AFFECTED = 'affected'

    STATUS = (
        (DESTROYED, 'Destroyed'),
        (AFFECTED, 'Affected'),
    )

    title = models.CharField(max_length=255, null=True, blank=True, default=None)
    type = models.ForeignKey(InfrastructureType, on_delete=models.PROTECT)
    status = models.CharField(max_length=25, choices=STATUS)
