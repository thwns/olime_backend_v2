"""
Serializers for recipe APIs
"""
from rest_framework import serializers

from core.models import (
    Track_Completion,
    Task,
)

from task import serializers as taskserializers


class Track_CompletionSerializer(serializers.ModelSerializer):
    """Serializer for track_completionss."""

    class Meta:
        model = Track_Completion
        fields = [
            'id', 'track_id', 'task_id', 'order_major', 'order_minor', 'complete_date',
        ]
        read_only_fields = ['id']


class Track_CompletionDetailSerializer(Track_CompletionSerializer):
    """Serializer for track_completion detail view."""

    class Meta(Track_CompletionSerializer.Meta):
        fields = Track_CompletionSerializer.Meta.fields + ['completed']
