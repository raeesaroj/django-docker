from rest_framework import viewsets
from .serializers import OrganizationSerializer,ProjectSerializer
from .models import Organization,Project


class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    search_fields = ('title', 'short_name', 'long_name')
    queryset = Organization.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    search_fields = ('title', 'ward')
    filter_fields = ('organization',)
    queryset = Project.objects.all()
