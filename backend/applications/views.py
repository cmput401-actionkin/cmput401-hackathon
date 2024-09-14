from rest_framework import viewsets
from .models import Applications, ChatMessage
from .serializers import ApplicationSerializer, ChatMessageSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

#@permission_classes([AllowAny])
class ApplicationsViewSet(viewsets.ModelViewSet):
    # queryset = Applications.objects.all()
    serializer_class = ApplicationSerializer

    # TODO: Filter by different categories - specific status, date applied, etc.
    def get_queryset(self):
        status = ""
        date_applied = ""
        companyname = ""
        position = ""

        if self.request.query_params.get('status'):
            status = self.request.query_params.get('status')
            return Applications.objects.filter(status=status)
        
        if self.request.query_params.get('date_applied'):
            date_applied = self.request.query_params.get('date_applied')
            return Applications.objects.filter(date_applied=date_applied) 
        
        if self.request.query_params.get('companyname'):
            companyname = self.request.query_params.get('companyname')
            return Applications.objects.filter(companyname=companyname)
        
        if self.request.query_params.get('position'):    
            position = self.request.query_params.get('position')
            return Applications.objects.filter(position=position)
        
        return Applications.objects.all()
        # return super().get_queryset()


# def applications(request):
#     return HttpResponse("Hello world!")

class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    # Chats for current user
    # def get_queryset(self):
    #     status = ""

    #     if self.request.query_params.get('status'):
    #         status = self.request.query_params.get('status')
    #         return Applications.objects.filter(status=status)
