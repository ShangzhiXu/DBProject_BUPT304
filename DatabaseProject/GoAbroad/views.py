from django.db import IntegrityError
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

        major = request.POST['major']
        majorAll = Major.objects.all()
        for x in majorAll:
            if(x.major == major):
                student.major = x
        student.type = request.POST['type']
        student.Rank = request.POST['rank']

        student.Hand_in_date = request.POST['handindate']
        student.get_offer_date = request.POST['getdate']

        program = request.POST['programname']
        programAll = Program.objects.all()
        for x in programAll :
            if (x.program_name == program):
                student.program_name  = x

        practice = request.POST['practicename']+" "+request.user.username
        practiceAll = Practice.objects.all()
        for x in practiceAll:
            if (x.company_name == practice):
                student.practice = x

        teacher_name= request.POST['teachername']
        teacherAll = Teacher.objects.all()
        for x in teacherAll:
            if (x.teacher_name ==  teacher_name):
                student.teacher_name = x

        school_name = request.POST['schoolname']
        schoolAll = School.objects.all()
        for x in schoolAll:
            if (x.school_name == school_name):
                student.school_name = x
        student.save()
    except(IntegrityError):
        return render(request, 'GoAbroad/bad.html', {
            'error_message': "请确认是否老师/专业/学校都已经在数据库中，没有请先填写再提交",
        })
    except (ValueError):
        return render(request, 'GoAbroad/input.html', {
            'error_message': "Please input all the blanks",
        })
    except (KeyError):
        return render(request, 'GoAbroad/input.html', {
            'error_message': "Please input all the blanks",
        })

    return render(request, 'GoAbroad/input.html', {
            'success_message': "Thanks for your input",
        })


def list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'blog_list.html', context)

def blog_detail(request,stu_id):
    student= get_object_or_404(Student,student_ID=stu_id)
    print(11111111)
    print(student.practice)
    context = {'ID': student.student_ID, 'GPA': student.GPA, 'major': student.major,
               'type': student.type, 'Rank': student.Rank,'scholarship':student.scholarship,
               'Hand_in_date' : student.Hand_in_date, 'get_offer_date':student.get_offer_date,
               'practice': student.practice,
               'program_name':student.program_name,'teacher_name':student.teacher_name,'school_name':student.school_name,
               'other':student.other
               }
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
        student_list = Student.objects.filter(major__major=question)
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
    elif select == 'program_name':
        student_list = Student.objects.filter(program_name=question)
    elif select == 'teacher_name':
        student_list = Student.objects.filter(teacher_name=question)
    elif select == 'school_name':
        student_list = Student.objects.filter(school_name=question)
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
            student_list1 = Student.objects.filter(major=major)
            student_list = merge(student_list1,student_list)
    print(student_list)
    if 'type' in request.GET:
        if request.GET['type'] :
            type = request.GET['type']
            student_list1 = Student.objects.filter(type__contains=type)
            student_list = merge(student_list1,student_list)
    print(student_list)
    if 'rank' in request.GET and 'rank1' in request.GET:
        if request.GET['rank'] and request.GET['rank1']:
            rank = request.GET['rank']
            rank1 = request.GET['rank1']
            student_list1 = Student.objects.filter(Rank__range=[rank, rank1])
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
            getdate = request.GET['getdate']
            getdate1 = request.GET['getdate1']
            student_list1 = Student.objects.filter(Hand_in_date__range=[getdate, getdate1])
            student_list = merge(student_list1, student_list)
    if 'program_name' in request.GET:
        if request.GET['program_name'] :
            program_name = request.GET['program_name']
            student_list1 = Student.objects.filter(program_name=program_name)
            student_list = merge(student_list1,student_list)
    if 'school_name' in request.GET:
        if request.GET['school_name'] :
            school_name = request.GET['school_name']
            student_list1 = Student.objects.filter(school_name=school_name)
            student_list = merge(student_list1,student_list)
    if 'teacher_name' in request.GET:
        if request.GET['teacher_name'] :
            teacher_name = request.GET['teacher_name']
            student_list1 = Student.objects.filter(teacher_name=teacher_name)
            student_list = merge(student_list1,student_list)

    context = {'students': student_list}
    return render(request, 'blog_list.html', context)

def practice(request):
    practice = Practice()
    try:
        practice.company_name = request.POST['company_name']+" "+request.user.username
        practice.leader_name = request.POST['leader_name']
        practice.work_time = request.POST['work_time']
        practice.payment = request.POST['payment']
        practice.house = request.POST['house']
        practice.rent = request.POST['rent']
        practice.save()
    except (KeyError):
        return render(request, 'GoAbroad/practice.html', {
            'error_message': "Please input all the blanks",
        })
    else:
        return render(request, 'GoAbroad/practice.html', {
            'success_message': "Thanks for your input",
        })
def put_teacher(request):
    teacher = Teacher()

    try:
        teacher.teacher_name = request.POST['teacher_name']
        major = request.POST['major']
        majorAll = Major.objects.all()
        for x in majorAll:
            if (x.major == major):
                teacher.major = x
        print(teacher.major)
        school_name = request.POST['school_name']
        schoolAll = School.objects.all()
        for x in schoolAll:
            if (x.school_name == school_name):
                teacher.school_name = x
        print(major)
        teacher.save()
    except (KeyError):
        return render(request, 'GoAbroad/put_teacher.html', {
            'error_message': "Please input all the blanks",
        })
    else:
        return render(request, 'GoAbroad/put_teacher.html', {
            'success_message': "Thanks for your input",
        })
def put_agent(request):
    agent = Agent()
    try:
        agent.agent_name = request.POST['agent_name']
        agent.cost = request.POST['cost']
        agent.evaluate = request.POST['evaluate']
        agent.save()
    except (KeyError):
        return render(request, 'GoAbroad/put_agent.html', {
            'error_message': "Please input all the blanks",
        })
    else:
        return render(request, 'GoAbroad/put_agent.html', {
            'success_message': "Thanks for your input",
        })
def test(request):
    return HttpResponse('test')


def teacher_detail(request,teacher_name):
    teacher= get_object_or_404(Teacher,teacher_name=teacher_name)
    context = {'Name': teacher.teacher_name, 'Major': teacher.major,'School': teacher.school_name
               }
    return render(request, 'teacher_detail.html', context)

def school_detail(request,school_name):
    school= get_object_or_404(School,school_name= school_name)
    context = {'Name': school.school_name,'qs_rank':school.qs_rank,'enrollment':school.enrollment,
               'final_number': school.final_number,'enrollment_for_bupt': school.enrollment_for_bupt
               }
    return render(request, 'school_detail.html', context)

def school_list(request):
    schools = School.objects.all()
    context = {'schools': schools}
    return render(request, 'school_list.html', context)

def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    print(teachers)
    return render(request, 'teacher_list.html', context)
