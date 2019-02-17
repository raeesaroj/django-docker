from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from polymorphic.models import PolymorphicModel

from federal.models import Ward


class Resource(PolymorphicModel):

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default=None)
    point = models.PointField(null=True, blank=True, default=None)
    ward = models.ForeignKey(
        Ward,
        related_name='resources',
        on_delete=models.PROTECT,
    )

    detail = JSONField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title


class Education(Resource):
    no_of_classrooms = models.PositiveIntegerField()


class Health(Resource):
    no_of_beds = models.PositiveIntegerField()
