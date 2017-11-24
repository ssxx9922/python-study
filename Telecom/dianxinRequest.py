#coding:utf-8

import requests
import time
import json
import random
import time
import dianxin1

wId = int(time.time()) % 1000

def get_svid():
    url = 'http://webwebfenxi.189.cn:9000/scode/live/ct189.js?v=' + str(int(time.time() * 1000))
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    response = requests.get(url)
    print('svid => ', response.cookies['svid'])
    return response.cookies['svid']

def send_fenxi(cookies):
    t = str(time.strftime("%d/%m/%Y %H:%M:%S %w ", time.localtime())) + '-480'
    url = 'http://webwebfenxi.189.cn:9000/b/ss/1/JS-1.5.1/s89421334611038?AQB=1&rsid=eshipeship-189-all&ndh=1&pf=1&t=' + t + '&fid=' + cookies['s_fid'] + '&ce=UTF-8&ns=eshipgdt&pageName=%2Flogin&g=http%3A%2F%2Flogin.189.cn%2Flogin&r=http%3A%2F%2Flogin.189.cn%2F&cc=CNY&ch=' + '其他' + '&events=event99%2Cevent8&c1=%2Flogin&v1=D%3Dvid&c2=D%3Dg&c3=' + '电信账号登录' + '&c4=login.189.cn&c6=D%3Dpid&c7=D%3Doid&c13=D%3Dt&c17=' + cookies['trkId'] + '&v17=%2Flogin&c18=20170106&c28=2224&s=1920x1080&c=24&j=1.6&v=N&k=Y&bw=1920&bh=314&AQE=1'
    response = requests.get(url,cookies=cookies)
    print('fenxi => ', response.text)

def verify_mobile(mobile,cookies):
    verify_Mobile_Url = 'http://login.189.cn/web/login/ajax'
    headers = {'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    body = {'m':'checkphone','phone':mobile}
    result = requests.post(verify_Mobile_Url,headers=headers,data=body,cookies=cookies)
    print(result.status_code)
    response = json.loads(result.text)
    print('省份ID => ',response['provinceId'])
    return response['provinceId']

def verify_get_code(mobile,provinceId,cookies):
    verify_get_code_Url = 'http://login.189.cn/web/login/ajax'
    headers = {'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    body = {'m':'captcha','account':mobile,'uType':'201','ProvinceID':provinceId}
    result = requests.post(verify_get_code_Url,headers=headers,data=body,cookies=cookies)
    print(result.status_code)
    response = json.loads(result.text)

def get_code_image(cookies):
    get_code_image_url = 'http://login.189.cn/web/captcha?undefined&source=login&width=100&height=37&' + str(random.random())
    response = requests.get(get_code_image_url,cookies=cookies)
    img = open('name' + '.jpg','wb+')
    img.write(response.content)
    img.close()
    print('image cookie => ',response.cookies)
    return response.cookies['EcsCaptchaKey']


def login(mobile,pwd,code,provinceId,cookies):
    login_url = 'http://login.189.cn/web/login'
    mpwd = dianxin1.process_pwd(pwd)
    headers = {'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
    body = {'AreaCode':'','CityNo':'','Account':mobile,'UType':'201','ProvinceID':provinceId,'RandomFlag':'0','Password':pwd,'Captcha':code}
    print(body)
    response = requests.post(login_url,headers=headers,cookies=cookies,data=body,allow_redirects=False)
    print(response.status_code)
    print(response.headers)
    id_url = response.headers['Location']

    response = requests.get(id_url,allow_redirects=False)
    print(response.status_code)
    print(response.headers['Set-Cookie'])


mobile = '18926089010'
pwd = 'TKcRwJjeQKQoa2JnvP8wPg=='

cookie = dianxin1.get_new_cookie()
provinceId = verify_mobile(mobile,cookie)
verify_get_code(mobile,provinceId,cookie)
key = get_code_image(cookie)
verify_get_code(mobile,provinceId,cookie)
print('key => ',key)
code = input('请输入验证码:')
cookie['EcsCaptchaKey']=key
cookie['ECS_ReqInfo_login1']='U2FsdGVkX18GO8qluxXHGMiR7UY5jbOAvdwS5dcqBPKfgz53R0ImTtKFiBK0IKgo+EflZ4RWauMxiX9wooelPGpmSEep++BTFSL51JHoHls='
login(mobile,pwd,code,provinceId,cookie)

