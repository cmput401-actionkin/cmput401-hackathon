from django.urls import include, path
from rest_framework import routers
from .views import ApplicationsViewSet

router = routers.DefaultRouter()
router.register(r'', ApplicationsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]