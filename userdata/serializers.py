"""
Serializers for profile APIs
"""
from rest_framework import serializers

from core.models import User_Data
from track.serializers import TrackDetailSerializer


class UserDataSerializer(serializers.ModelSerializer):
    """Serializer for userdatas."""
    track = TrackDetailSerializer(read_only=True)
    #task = Taskserializers.TaskDetailSerializer(read_only=True)

    class Meta:
        model = User_Data
        fields = [
            'id', 'track', 'action_date',
         ]
        read_only_fields = ['id']


class UserDataDetailSerializer(UserDataSerializer):
    """Serializer for UserData detail view."""

    class Meta(UserDataSerializer.Meta):
        fields = UserDataSerializer.Meta.fields + ['is_done']