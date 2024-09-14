from rest_framework import serializers
from .models import Applications

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Applications
        fields = ['companyname', 'position', 'date_applied', 'status']