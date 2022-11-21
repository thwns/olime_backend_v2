"""
Serializers for task APIs
"""
from rest_framework import serializers
from core.models import Track_Star_Point


class Track_Star_PointSerializer(serializers.ModelSerializer):
    """Serializer for Track_Star_Points."""

    class Meta:
        model = Track_Star_Point
        fields = [
            'id', 'track_id',
        ]
        read_only_fields = ['id']


class Track_Star_PointDetailSerializer(Track_Star_PointSerializer):
    """Serializer for Track_Star_Point detail view."""

    class Meta(Track_Star_PointSerializer.Meta):
        fields = Track_Star_PointSerializer.Meta.fields + ['star_point']
