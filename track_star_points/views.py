"""
Views for the Content_Star_Point APIs
"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Track_Star_Point
from track_star_points import serializers
# Create your views here.


class Track_Star_PointViewSet(viewsets.ModelViewSet):
    """View for manage Track_Star_Point APIs."""
    serializer_class = serializers.Track_Star_PointDetailSerializer
    queryset = Track_Star_Point.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve profiles for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.Track_Star_PointSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new Track_Star_Point."""
        serializer.save(user=self.request.user)


class Track_Star_PointAllViewSet(viewsets.ModelViewSet):
    queryset = Track_Star_Point.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['track_id']

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return serializers.Track_Star_PointDetailSerializer
