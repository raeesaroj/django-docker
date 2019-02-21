from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    resource_type = serializers.SlugRelatedField(
        read_only=True,
        slug_field='model',
        source='polymorphic_ctype',
    )

    class Meta:
        model = Resource
        fields = ('title', 'description', 'point', 'ward', 'resource_type')
