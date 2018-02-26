from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from users.forms import LoginForm, RegisterForm, FergetPwdForm, ResetPwdForm
from .models import UserProfile, EmailVerifyRecord

from utils.email_send import send_register_email

# Create your views here.
class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username')
            pass_word = request.POST.get('password')
            user = authenticate(username = user_name, password = pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html', {})
                else:
                    return render(request, 'login.html', {'msg':'用户名或密码错误'})
            else:
                return render(request, 'login.html', {'msg':'用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form':login_form})

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})
    def post(self, request):
        # captcha = request.POST.get('captcha')
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'msg': '用户已经注册','register_form':register_form})
            pass_word = request.POST.get('password')
            user_profile = UserProfile.objects.create_user(user_name, user_name, pass_word)
            user_profile.is_active = False
            user_profile.save()

            send_register_email(email=user_name,send_type='register')

            return render(request, 'login.html', {})
        else:
            return render(request, 'register.html', {'register_form':register_form})


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')

class ForgetPwdView(View):
    def get(self,request):
        forgetpwd_form = RegisterForm()
        return render(request, 'forgetpwd.html', {'forgetpwd_form':forgetpwd_form})

    def post(self, request):
        forgetpwd_form = FergetPwdForm(request.POST)
        if forgetpwd_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, 'forget')
            return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {'forgetpwd_form': forgetpwd_form})

class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {'email':email})
        else:
            return render(request, 'index.html')

    def post(self, request):
        modify_form = ResetPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password1', '')
            email = request.POST.get('email', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email, 'msg':'密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()

            return render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request, 'login.html', {'email': email})
