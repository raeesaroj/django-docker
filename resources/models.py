from django.contrib.gis.db import models
from federal.models import Ward
from django.contrib.postgres.fields import JSONField


class Resource(models.Model):

    HEALTH = 'health'
    EDUCATION = 'education'
    TOURISM = 'tourism'

    TYPES = (
        (HEALTH, 'health'),
        (EDUCATION, 'education'),
        (TOURISM, 'tourism'),
    )

    name = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True, default=None)
    type = models.CharField(max_length=25, choices=TYPES)
    point = models.PointField(null=True, blank=True, default=None)
    ward = models.ForeignKey(
        Ward,
        related_name='resources',
        on_delete=models.PROTECT,
    )
    # TODO: separate tables
    detail = JSONField(null=True, blank=True, default=None)
