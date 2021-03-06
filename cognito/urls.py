"""cognito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from cognito import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', view=views.get_tutor_page, name="get tutor info"),
    url('^tutors$', view=views.get_tutor_page, name="get tutor info"),
    url('^installed$', view=views.installed, name="installed"),
    url('^logout/$', view=views.logout, name="logout"),
    url(r'^api-token-auth/', obtain_jwt_token),
]
