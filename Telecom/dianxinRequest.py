#coding:utf-8

import requests
import time
import json
import random

import dianxin1

wId = int(time.time()) % 1000


def verify_mobile(mobile):
    verify_Mobile_Url = 'http://login.189.cn/web/login/ajax'
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    body = {'m':'checkphone','phone':mobile}
    result = requests.post(verify_Mobile_Url,headers=headers,data=body)
    print(result.status_code)
    response = json.loads(result.text)
    print(response['provinceId'])

def verify_get_code(mobile):
    verify_get_code_Url = 'http://login.189.cn/web/login/ajax'
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    body = {'m':'captcha','account':mobile,'uType':'201','ProvinceID':'14'}
    result = requests.post(verify_get_code_Url,headers=headers,data=body)
    print(result.status_code)
    response = json.loads(result.text)
    print(response)

def get_code_image():
    get_code_image_url = 'http://login.189.cn/web/captcha?undefined&source=login&width=100&height=37&' + str(random.random())
    response = requests.get(get_code_image_url)
    print(response.cookies)
    img = open('name' + '.jpg','wb+')
    img.write(response.content)
    img.close()

def login(mobile,pwd,code):
    login_url = 'http://login.189.cn/web/login'
    mpwd = dianxin1.process_pwd(pwd)
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    body = {'m':'captcha','Account':mobile,'UType':'201','ProvinceID':'14','RandomFlag':'','Password':mpwd,'Captcha':code}
    print(body)
    cookies = {}
    response = requests.post(login_url,headers=headers,data=body,cookies=cookies)
    # print(response.text)

login('18050055118','518316','1234')

