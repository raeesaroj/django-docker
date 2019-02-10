from django.db import models
from bipad.models import TimeStampedModal
from django.contrib.postgres.fields import JSONField
from resources.models import Resource


class Hazard(TimeStampedModal):

    title = models.CharField(max_length=250)
    description = models.TextField()
    icon = models.FileField(upload_to='hazard-icons/')
    style = JSONField(default=None, null=True, blank=True)
    related_resources = models.ManyToManyField(Resource)

    def __str__(self):
        return self.title
