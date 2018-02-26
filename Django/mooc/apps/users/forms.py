#_*_ coding:utf-8 _*_
from captcha.fields import CaptchaField

__author__ = 'Harryue'
__date__ = '2018/2/24 AM10:43'

from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=3, max_length=21)
    password = forms.CharField(required=True, min_length=5, max_length=21)

class RegisterForm(forms.Form):
    username = forms.EmailField(required=True, min_length=3, max_length=21)
    password = forms.CharField(required=True, min_length=5, max_length=21)
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})


class FergetPwdForm(forms.Form):
    username = forms.EmailField(required=True, min_length=3, max_length=21)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})

class ResetPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5, max_length=21)
    password2 = forms.CharField(required=True, min_length=5, max_length=21)