"""DatabaseProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.user_logout, name='login_out'),
    path('login/', views.login, name='login'),
    path('login_context/', views.login_context, name='login_context'),
    path('register/', views.register, name='register'),
    path('register_context/', views.register_context, name='register_context'),
    path('input/', views.input, name='input'),
    path('list/', views.list, name='list'),
    path('detail/<int:stu_id>/',views.blog_detail,name='blog_detail'),
]