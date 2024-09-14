from rest_framework import serializers
from .models import Notifications


class NotificationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notifications
        fields = ['companyname', 'position', 'date_applied', 'status','message']