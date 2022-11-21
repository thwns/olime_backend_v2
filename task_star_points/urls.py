"""
URL mappings for the profile app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from task_star_points import views


router = DefaultRouter()
router.register('task_star_points', views.Task_Star_PointViewSet)
router.register('task_star_points_alls', views.Task_Star_PointAllViewSet)

app_name = 'task_star_points'

urlpatterns = [
    path('', include(router.urls)),
]
