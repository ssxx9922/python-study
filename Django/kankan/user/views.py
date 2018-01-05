from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return HttpResponse('hello')

def register(request):
    return HttpResponse('register')

def find_pwd(request):
    return HttpResponse('findpwd')