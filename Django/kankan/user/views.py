from django.shortcuts import render
from django.http import HttpResponse
from . import models


def info(request):
    user = models.user.objects.get(id='1')
    return render(request, 'user/index.html', {'data': user})


def login(request):
    phone = request.GET.get('phone')
    password = request.GET.get('password')
    return HttpResponse(phone+password)

def register(request):
    return HttpResponse('register')

def find_pwd(request):
    return HttpResponse('findpwd')