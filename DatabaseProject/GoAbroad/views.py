from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

def home(request):
    return render(request, 'GoAbroad/home.html')

def login(request):
    return render(request, 'GoAbroad/login.html')
def login_context(request):

    request.encoding = 'utf-8'
    username = ""
    pwd = ""
    if 'username' in request.GET :
        username = request.GET['username']
    if 'pwd' in request.GET :
        pwd = request.GET['pwd']
    #登陆
    user = auth.authenticate(username=username, password=pwd)
    auth.login(request, user)
    if username == 'admin':
        print(username)
        # 确定是admin还是user，跳转到不同的页面
        return render(request, 'admin/', {
            'username': username,
        })
    else:
        return render(request, 'GoAbroad/login.html',{
            'username':username,
        })

def register(request):
    return render(request, 'GoAbroad/register.html')


def is_valid(username, pwd):
    return True


def register_context(request):
    request.encoding = 'utf-8'
    username = ""
    pwd = ""
    if 'username' in request.GET :
        username = request.GET['username']
    if 'pwd' in request.GET :
        pwd = request.GET['pwd']
    #todo  确定是否符合数据库中用户名密码匹配，如果匹配，返回错误信息
    if is_valid(username,pwd):
        # 注册
        user = User.objects.create_user(username,"",pwd)
        user.save()
        # 登录
        user = auth.authenticate(username=username, password=pwd)
        auth.login(request, user)
    return render(request, 'GoAbroad/register.html',{
            'username':username,
        })

def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/GoAbroad/")

def input(request):
    student = Student()
    try:
        student.student_ID = request.user.username
        student.GPA = request.POST['GPA']
        student.major = request.POST['major']
        student.type = request.POST['type']
        student.Rank = request.POST['rank']
        student.Hand_in_date = request.POST['handindate']
        student.get_offer_date = request.POST['getdate']
        student.save()
    except (KeyError):
        return render(request, 'GoAbroad/input.html', {
            'error_message': "Please input all the blanks",
        })
    else:
        return render(request, 'GoAbroad/input.html', {
            'success_message': "Thanks for your input",
        })


def list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'blog_list.html', context)

def blog_detail(request,stu_id):
    print(stu_id)
    student= get_object_or_404(Student,student_ID=stu_id)
    context = {'ID': student.student_ID, 'GPA': student.GPA, 'major': student.major,
               'type': student.type, 'Rank': student.Rank,'scholarship':student.scholarship,
               'Hand_in_date' : student.Hand_in_date, 'get_offer_date':student.get_offer_date}
    return render(request, 'blog_detail.html', context)