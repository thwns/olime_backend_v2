"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from contents import views


router = DefaultRouter()
router.register('contents', views.ContentViewSet)
router.register('contents_alls', views.ContentAllViewSet)

app_name = 'contents'

urlpatterns = [
    path('', include(router.urls)),
]
