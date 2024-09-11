from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, LabelViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'labels', LabelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
