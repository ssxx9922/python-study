from django.urls import path

from . import views

urlpatterns = [
    path('info/',views.info),
    path('login/', views.login),
    path('register/', views.register),
    path('findpwd/', views.find_pwd),
]