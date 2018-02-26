#_*_ coding:utf-8 _*_
__author__ = 'Harryue'
__date__ = '2018/2/26 PM3:28'

from random import Random
from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from mooc.settings import EMAIL_HOST_USER

def random_str(randomlength=8):
    str = ''
    chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_code = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '注册激活链接'
        email_body = '点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_HOST_USER, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '重置密码'
        email_body = '点击下面的链接重置密码：http://127.0.0.1:8000/reset/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_HOST_USER, [email])
        if send_status:
            pass



