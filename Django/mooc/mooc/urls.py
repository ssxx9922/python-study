"""mooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin
# from mooc.settings import STATIC_ROOT

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forgetpwd/', ForgetPwdView.as_view(), name='forget_pwd'),
    path('captcha/', include('captcha.urls')),
    path('active/<str:active_code>/', ActiveUserView.as_view(), name='userActive'),
    path('reset/<str:active_code>/', ResetView.as_view(), name='userReset'),
    # path('static/<str:path>/', serve, {'document_root', STATIC_ROOT})
    # path('users/', include('users.urls')),
    # path('courses/', include('courses.urls')),
    # path('organization/', include('organization.urls')),
    # path('operation/', include('operation.urls'))
]

handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
