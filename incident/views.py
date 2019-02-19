from rest_framework import (
    viewsets,
)
from .serializers import IncidentSerializer
from .models import Incident


class IncidentViewSet(viewsets.ModelViewSet):
    serializer_class = IncidentSerializer
    search_fields = ('title',)
    queryset = Incident.objects.filter(verified=True)
