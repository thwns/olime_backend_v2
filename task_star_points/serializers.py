"""
Serializers for task_star_point APIs
"""
from rest_framework import serializers
from core.models import Task_Star_Point


class Task_Star_PointSerializer(serializers.ModelSerializer):
    """Serializer for Task_Star_Points."""

    class Meta:
        model = Task_Star_Point
        fields = [
            'id', 'task_id',
        ]
        read_only_fields = ['id']


class Task_Star_PointDetailSerializer(Task_Star_PointSerializer):
    """Serializer for Task_Star_Point detail view."""

    class Meta(Task_Star_PointSerializer.Meta):
        fields = Task_Star_PointSerializer.Meta.fields + ['star_point']
