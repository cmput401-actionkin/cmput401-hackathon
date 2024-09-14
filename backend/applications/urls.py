from django.urls import include, path
from . import views
from rest_framework import routers
from .views import ApplicationsViewSet, ChatMessageViewSet

router = routers.DefaultRouter()
router.register(r'', ApplicationsViewSet, basename='applications')
router.register(r'chat', ChatMessageViewSet, basename='chatmessages')

urlpatterns = [
    path('', include(router.urls)),
]