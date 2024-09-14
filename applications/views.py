
from rest_framework import viewsets
from .models import Applications

from .serializers import ApplicationSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

#@permission_classes([AllowAny])
class ApplicationsViewSet(viewsets.ModelViewSet):
    queryset = Applications.objects.all()
    serializer_class = ApplicationSerializer


# def applications(request):
#     return HttpResponse("Hello world!")