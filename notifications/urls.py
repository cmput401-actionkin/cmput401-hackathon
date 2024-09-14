from django.urls import include, path
from . import views
from rest_framework import routers
from .views import NotificationsViewSet

router = routers.DefaultRouter()
router.register(r'', NotificationsViewSet)


urlpatterns = [
    path('', include(router.urls)),

]