"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from track_completions import views


router = DefaultRouter()
router.register('track_completions', views.Track_CompletionViewSet)

app_name = 'track_completions'

urlpatterns = [
    path('', include(router.urls)),
]
