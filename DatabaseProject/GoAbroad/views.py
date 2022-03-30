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
    student= get_object_or_404(Student,student_ID=stu_id)
    context = {'ID': student.student_ID, 'GPA': student.GPA, 'major': student.major,
               'type': student.type, 'Rank': student.Rank,'scholarship':student.scholarship,
               'Hand_in_date' : student.Hand_in_date, 'get_offer_date':student.get_offer_date}
    return render(request, 'blog_detail.html', context)


def search(request):
    question = ''
    select = ''
    student_list = []
    if 'q' in request.GET :
        question = request.GET['q']
    if 'select' in request.GET :
        select= request.GET['select']
    error_msg = ''

    if not question:
        error_msg = '请输入关键词'
        return HttpResponse(error_msg)
    if select == 'student_ID':
        student_list = Student.objects.filter(student_ID__icontains=question)
    elif select == 'major':
        student_list = Student.objects.filter(major__icontains=question)
    elif select == 'type':
        student_list = Student.objects.filter(type__icontains=question)
    elif select == 'GPA':
        student_list = Student.objects.filter(GPA__icontains=question)
    elif select == 'scholarship':
        student_list = Student.objects.filter(scholarship__icontains=question)
    elif select == 'Hand_in_date':
        student_list = Student.objects.filter(Hand_in_date__icontains=question)
    elif select == 'get_offer_date':
        student_list = Student.objects.filter(get_offer_date__icontains=question)

    context = {'students': student_list}
    return render(request, 'blog_list.html', context)


def adv_search(request):
    return render(request, 'search.html')


def merge(student_list1, student_list):
    returnlist = []
    for item in student_list:
        if item in student_list1:
            returnlist.append(item)
    return returnlist


def adv_search_context(request):
    request.encoding = 'utf-8'
    question = ''
    select = ''
    student_list = Student.objects.all()
    if 'GPA' in request.GET and 'GPA1' in request.GET:
        if request.GET['GPA'] and request.GET['GPA1']:
            gpa = request.GET['GPA']
            gpa1 = request.GET['GPA1']
            student_list = Student.objects.filter(GPA__range=[gpa, gpa1])
    print(student_list)
    if 'major' in request.GET:
        if request.GET['major']:
            major = request.GET['major']
            student_list1 = Student.objects.filter(major__icontains=major)
            student_list = merge(student_list1,student_list)
    print(student_list)
    if 'type' in request.GET:
        if request.GET['type'] :
            type = request.GET['type']
            student_list1 = Student.objects.filter(type__icontains=type)
            student_list = merge(student_list1,student_list)
    print(student_list)
    if 'rank' in request.GET and 'rank1' in request.GET:
        if request.GET['rank'] and request.GET['rank1']:
            rank = request.GET['rank']
            rank1 = request.GET['rank1']
            student_list1 = Student.objects.filter(rank__range=[rank, rank1])
            student_list = merge(student_list1, student_list)
    print(student_list)
    if 'handindate' in request.GET and 'handindate1' in request.GET:
        if request.GET['handindate'] and request.GET['handindate1']:
            handindate = request.GET['handindate']
            handindate1 = request.GET['handindate1']
            student_list1 = Student.objects.filter(Hand_in_date__range=[handindate, handindate1])
            student_list = merge(student_list1, student_list)
    print(student_list)
    if 'getdate' in request.GET and 'getdate1' in request.GET:
        if request.GET['getdate'] and request.GET['getdate1']:
            getdate = request.GET['getdatedate']
            getdate1 = request.GET['getdatedate1']
            student_list1 = Student.objects.filter(Hand_in_date__range=[getdate, getdate1])
            student_list = merge(student_list1, student_list)
    print(student_list)
    context = {'students': student_list}
    return render(request, 'blog_list.html', context)
