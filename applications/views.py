
from rest_framework import viewsets
from .models import Applications
from .serializers import ApplicationSerializer
from rest_framework import generics


class ApplicationsViewSet(viewsets.ModelViewSet):
    queryset = Applications.objects.all()
    serializer_class = ApplicationSerializer


# def applications(request):
#     return HttpResponse("Hello world!")