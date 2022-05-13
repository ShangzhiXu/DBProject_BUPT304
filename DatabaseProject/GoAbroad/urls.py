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
    path('delete/<str:stu_id>/', views.delete, name='delete'),
    path('detail/<str:stu_id>/',views.blog_detail,name='blog_detail'),
    path('search/', views.search, name='search'),
    path('adv_search/', views.adv_search, name='adv_search'),
    path('adv_search_context/', views.adv_search_context, name='adv_search_context'),
    #用户填写实习信息界面
    path('practice/', views.practice, name='practice'),
    #用户填写老师信息界面
    path('put_teacher/', views.put_teacher, name='put_teacher'),
    #用户填写中介信息界面
    path('put_agent/', views.put_agent, name='put_agent'),
    path('test/', views.test, name='test'),
    path('teacher_detail/<str:teacher_name>/',views.teacher_detail,name='teacher_detail'),
    path('school_detail/<str:school_name>/',views.school_detail,name='school_detail'),
    path('school_list/', views.school_list, name='school_list'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
]