from django.db import models
from federal.models import Ward


class Organization(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    ward = models.ManyToManyField(Ward, related_name='ward')

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
