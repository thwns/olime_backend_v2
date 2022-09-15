"""
Views for the track APIs
"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Max

from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Track_Completion,
    Book,
    Task,

)
from track_completions import serializers
from task import serializers as taskserializers
from book import serializers as bookserializers


class Track_CompletionViewSet(viewsets.ModelViewSet):
    """View for manage track_completion APIs."""
    serializer_class = serializers.Track_CompletionDetailSerializer
    queryset = Track_Completion.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed']

    def get_queryset(self):
        """Retrieve track_completions for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.Track_CompletionDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new track_completion."""
        serializer.save(user=self.request.user)


'''class Track_CompletionAllViewSet(viewsets.ModelViewSet):
    """View for manage track_completion APIs."""
    serializer_class = serializers.Track_CompletionDetailSerializer
    queryset = Track_Completion.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve track_completions for authenticated user."""
        if self.queryset.filter(user=self.request.user, completed=True).order_by('-id') == []:
            return self.queryset.aggregate(Max('order_major')+1)
        else:
            return [self.queryset.filter(user=self.request.user, completed=False).order_by('-id'),
                    self.queryset.aggregate(Max('order_major')+1)]

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.Track_CompletionDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new track_completion."""
        serializer.save(user=self.request.user)'''
