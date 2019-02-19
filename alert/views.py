from django.utils import timezone
from rest_framework import viewsets
from .serializers import AlertSerializer
from .models import Alert


class AlertViewSet(viewsets.ModelViewSet):
    serializer_class = AlertSerializer
    search_fields = ('title',)
    filter_fields = ('hazard', 'event')
    queryset = Alert.objects.filter(verified=True).exclude(
        expire_on__lte=timezone.now()
    )
