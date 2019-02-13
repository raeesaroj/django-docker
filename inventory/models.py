from django.db import models
from bipad.models import TimeStampedModal
from resources.models import Resource


class Inventory(TimeStampedModal):

    KG = 'kg'
    LITRE = 'litre'
    METER_SQUARE = 'm2'
    PCS = 'pcs'

    SCALES = (
        (KG, 'KG'),
        (LITRE, 'Litre'),
        (METER_SQUARE, 'm2'),
        (PCS, 'PCS'),
    )
    title = models.CharField(max_length=255)
    amount = models.IntegerField()
    scale = models.CharField(max_length=25, choices=SCALES)
    resource = models.ForeignKey(
        Resource,
        related_name='inventories',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "inventories"
