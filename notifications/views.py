
from rest_framework import viewsets
from .models import Notifications
from .serializers import NotificationsSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny



class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer


# def applications(request):
#     return HttpResponse("Hello world!")