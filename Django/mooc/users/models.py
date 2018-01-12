from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class UserProfile(AbstractUser):
    choices_gender = (
        ('male','男'),
        ('demale','女')
    )
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='wow')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(choices=choices_gender,default='male',max_length=10)
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    header_image = models.ImageField(upload_to='image/%Y/%m', default='')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    send_code = models.CharField(choices=(('register', '注册'),('forget', '找回密码')), max_length=10, verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='加入时间')

    def __str__(self):
        return '(' + self.email + ')' + self.code

    class Mate:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图', default='')
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Mate:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name