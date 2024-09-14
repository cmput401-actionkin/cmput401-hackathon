from rest_framework import serializers
from .models import Applications, ChatMessage

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Applications
        fields = ['companyname', 'position', 'date_applied', 'status']

class ChatMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['author', 'receiver', 'message', 'timestamp']