from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
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
    #todo  确定是否符合数据库中用户名密码匹配

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
    return HttpResponse("This is the register in page")

def input(request):
    student = Student()
    try:
        student.student_ID = 1
        student.GPA = request.POST['GPA']
        student.major = request.POST['major']
        student.type = request.POST['type']
        student.Rank = request.POST['rank']
        student.Hand_in_date = request.POST['handindate']
        student.get_offer_date = request.POST['getdate']

    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'GoAbroad/input.html', {
            'error_message': "Please input all the blanks",
        })
    else:
        return render(request, 'GoAbroad/input.html', {
            'success_message': "Thanks for your input",
        })

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('GoAbroad:results', args=(question.id,)))