"""
URL mappings for the profile app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from content_star_points import views


router = DefaultRouter()
router.register('content_star_points', views.Content_Star_PointViewSet)
router.register('content_star_points_alls', views.Content_Star_PointAllViewSet)

app_name = 'content_star_points'

urlpatterns = [
    path('', include(router.urls)),
]
