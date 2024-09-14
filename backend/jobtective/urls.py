"""
URL configuration for jobtective project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from applications.models import Applications
from notifications.models import Notifications
from rest_framework.authtoken.views import obtain_auth_token  # DRF's built-in token auth view
from register.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applications/', include('applications.urls')),
    path('notifications/', include('notifications.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/register/', register, name='register'), 
]
