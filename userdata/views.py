"""
Views for the userdata APIs
"""
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import User_Data
from userdata import serializers
# Create your views here.


class UserDataViewSet(viewsets.ModelViewSet):
    """View for manage userdata APIs."""
    serializer_class = serializers.UserDataDetailSerializer
    queryset = User_Data.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve profiles for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.UserDataSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new userdata."""
        serializer.save(user=self.request.user)


class UserDataTrackList(viewsets.ModelViewSet):
    """View for userdata tracks APIs."""
    serializer_class = serializers.UserDataDetailSerializer
    queryset = User_Data.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """View for userdata tracks list"""
        queryset = User_Data.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.UserDataSerializer

        return self.serializer_class
