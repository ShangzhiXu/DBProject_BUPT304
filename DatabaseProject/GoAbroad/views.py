from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import *

def home(request):
    student_list = Student.objects.order_by('id')[:5]
    template = loader.get_template('GoAbroad/home.html')
    context = {
        'student_list': student_list,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    return HttpResponse("This is the log in page")

def register(request):
    return HttpResponse("This is the register in page")

