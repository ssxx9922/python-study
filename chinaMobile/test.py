#coding:utf-8

import requests
import json
import math
import random
import time

def get_w():
    co_f='2'
    curt=str(int(time.time()*1000))
    for i in range(1,32-len(curt)):
	    co_f+=hex(math.floor(random.random()*16))[-1]
    co_f+=curt
    return 'id=' + co_f + ':lv=' + curt + ':ss=' + curt

def send_code(mobile):
    url = 'http://bj.ac.10086.cn/ac/tempPwdSend'
    data = {
        'mobile':mobile
    }
    response = requests.post(url,data=data)
    print('发送验证码：',response.status_code,response.text,response.headers)

    JSESSIONID = response.cookies['JSESSIONID']
    Webtrends = response.cookies['Webtrends']
    cookie = {
        'JSESSIONID':JSESSIONID,
        'Webtrends':Webtrends,
    }
    return cookie

def validate(mobile,cookies):
    url = 'http://bj.ac.10086.cn/ac/ValidateIp'
    data = {
        'ceshi':'false'
    }
    response = requests.post(url,data=data,cookies=cookies)
    print('validate 请求结果:',response.status_code,response.text,response.headers)

def login(mobile, code,cookies):
    url = 'http://bj.ac.10086.cn/ac/CmSsoLogin'
    data = {
        'user': mobile,
        'phone': mobile,
        'backurl': 'http://www.bj.10086.cn/my',
        'continue':'http://www.bj.10086.cn/my',
        'style':'BIZ_LOGINBOX',
		'service':'www.bj.10086.cn',
		'box':'',
        'ssoLogin':'yes',
        'loginMode': 2,
        'loginMethod': 1,
        'loginName': mobile,
        'target':'_parent',
		'password':'',
        'smsNum': code,
        'rnum':'',
        'ckCookie': 'on',
    }
    headers = {
        'Host':'bj.ac.10086.cn',
		'Connection':'keep-alive',
		'Content-Length':'285',
		'Cache-Control':'max-age=0',
		'Origin':'https://bj.ac.10086.cn',
		'Upgrade-Insecure-Requests':'1',
		'Content-Type':'application/x-www-form-urlencoded',
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Referer':'https://bj.ac.10086.cn/ac/cmsso/iloginnew.jsp',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    }
    response = requests.post(url, data=data, headers=headers, cookies=cookies, allow_redirects=False)
    print('北京移动，登录：', mobile, response.status_code, response.headers)

    newurl = response.headers['Location']
    response1 = requests.get(newurl, cookies=cookies)
    print('北京移动，登录第二步：', mobile, response1.status_code, response1.headers)

mobile = '15011463580'
cookies = send_code(mobile)
code = input('code=')
cookies['WT_FPC'] = get_w()
cookies['login_mobile'] = mobile
cookies['c_mobile'] = mobile
validate(mobile,cookies)
login(mobile,code,cookies)

