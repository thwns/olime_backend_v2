"""
Serializers for task APIs
"""
from rest_framework import serializers
from core.models import Content_Star_Point


class Content_Star_PointSerializer(serializers.ModelSerializer):
    """Serializer for Content_Star_Points."""

    class Meta:
        model = Content_Star_Point
        fields = [
            'id', 'content_id',
        ]
        read_only_fields = ['id']


class Content_Star_PointDetailSerializer(Content_Star_PointSerializer):
    """Serializer for Content_Star_Point detail view."""

    class Meta(Content_Star_PointSerializer.Meta):
        fields = Content_Star_PointSerializer.Meta.fields + ['star_point']
