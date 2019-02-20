from django.utils import timezone
from rest_framework import viewsets
from .serializers import ProvinceSerializer, DistrictSerializer, MunicipalitySerializer, WardSerializer
from .models import Province, District, Municipality, Ward


class ProvinceViewSet(viewsets.ModelViewSet):
    serializer_class = ProvinceSerializer
    search_fields = ('title',)
    queryset = Province.objects.all()


class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer
    search_fields = ('title',)
    filter_fields = ('province',)
    queryset = District.objects.all()


class MunicipalityViewSet(viewsets.ModelViewSet):
    serializer_class = MunicipalitySerializer
    search_fields = ('title',)
    filter_fields = ('district',)
    queryset = Municipality.objects.all()


class WardViewSet(viewsets.ModelViewSet):
    serializer_class = WardSerializer
    search_fields = ('title',)
    filter_fields = ('municipality',)
    queryset = Ward.objects.all()
