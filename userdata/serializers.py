"""
Serializers for profile APIs
"""
from rest_framework import serializers

from core.models import User_Data


class UserDataSerializer(serializers.ModelSerializer):
    """Serializer for userdatas."""

    class Meta:
        model = User_Data
        fields = [
            'id', 'track_id', 'task_id', 'action_date',
        ]
        read_only_fields = ['id']


class UserDataDetailSerializer(UserDataSerializer):
    """Serializer for UserData detail view."""

    class Meta(UserDataSerializer.Meta):
        fields = UserDataSerializer.Meta.fields + ['is_done']
