from django.db import models


class TestModel(models.Model):

    description = models.TextField(null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = "Test"

