"""
URL mappings for the profile app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from track_star_points import views


router = DefaultRouter()
router.register('track_star_points', views.Track_Star_PointViewSet)
router.register('track_star_points_alls', views.Track_Star_PointAllViewSet)

app_name = 'track_star_points'

urlpatterns = [
    path('', include(router.urls)),
]
