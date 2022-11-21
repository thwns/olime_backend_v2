"""
Views for the Content_Star_Point APIs
"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Content_Star_Point
from content_star_points import serializers
# Create your views here.


class Content_Star_PointViewSet(viewsets.ModelViewSet):
    """View for manage Content_Star_Point APIs."""
    serializer_class = serializers.Content_Star_PointDetailSerializer
    queryset = Content_Star_Point.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve profiles for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.Content_Star_PointSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new Content_Star_Point."""
        serializer.save(user=self.request.user)


class Content_Star_PointAllViewSet(viewsets.ModelViewSet):
    queryset = Content_Star_Point.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['content_id']

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return serializers.Content_Star_PointDetailSerializer
