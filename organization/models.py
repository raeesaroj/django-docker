from django.db import models
from federal.models import Ward


class Organization(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    ward = models.ManyToManyField(Ward, related_name='ward')
