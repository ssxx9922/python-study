#coding:utf-8

import requests
import time
import json
import random

#  登录-发验证码
def get_verify_code_image(mobile):
    url = 'https://login.10086.cn/captchazh.htm?type=05&timestamp=' + str(int(time.time()*1000))
    response = requests.get(url,verify=False)
    img = open(mobile + '1.jpg','wb+')
    img.write(response.content)
    img.close()
    cookies = {}
    cookies['rdmdmd5'] = response.cookies['rdmdmd5']
    cookies['CaptchaCode'] = response.cookies['CaptchaCode']
    return cookies
# 登录-验证验证码
def verify_code(code,cookies):
    url = 'https://login.10086.cn/verifyCaptcha?inputCode=' + code
    response = requests.get(url,cookies=cookies,verify=False)
    print('验证码验证结果 => ',response.text)

# 登录-检验是否是北京手机号
def chick_bj_mobile(mobile):
    url = 'https://login.10086.cn/chkNumberAction.action'
    data = {
        'userName':mobile
    }
    headers = {
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
    response = requests.post(url,headers=headers,data=data,verify=False)
    print('验证是否北京移动 => ','成功' if response.text == 'true' else '失败')
    
# 登录-发送验证码
def send_code(mobile):
    url = 'https://login.10086.cn/sendRandomCodeAction.action'
    data = {
        'userName':mobile,
        'channelID':'12003',
        'type':'01'
    }
    headers = {
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
    response = requests.post(url,headers=headers,data=data,verify=False)
    # 0 - 成功  1 - 失败  2 - 超过次数
    print('发送短信是否成功 => ','成功' if response.text == '0' else '失败')

# 登录
def login(mobile,pwd,smsPwd):
    url = 'http://login.10086.cn/login.htm?accountType=01&account='+ mobile +'&password='+pwd+'&pwdType=01&smsPwd='+smsPwd+'&inputCode=&backUrl=http%3A%2F%2Fshop.10086.cn%2Fi%2Fsso.html&rememberMe=0&channelID=12003&protocol=https%3A'
    headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Referer': 'https://login.10086.cn/html/window/loginMini.html?channelID=12003&backUrl=http://shop.10086.cn/i/sso.html',
    }
    print(url)
    response = requests.get(url,headers=headers,verify=False)
    print(response.status_code,response.text)
    print(response.headers)
    result = json.loads(response.text)
    cookies = {}
    cookies['is_login'] = response.headers['is_login']
    cookies['userinfokey'] = response.headers['userinfokey']
    cookies['verifyCode'] = response.headers['verifyCode']
    cookies['c'] = response.headers['c']
    newUrl = result['assertAcceptURL'] + 'backUrl=http://shop.10086.cn/i/sso.html&artifact=' + result['artifact']
    newResponse = requests.get(newUrl,cookies=cookies,verify=False,allow_redirects=False)
    print(newResponse.cookies)
    cookies['jsessionid-echd-cpt-cmcc-jt'] = newRespons.cookies['jsessionid-echd-cpt-cmcc-jt']
    cookies['ssologinprovince'] = newResponse.cookies['ssologinprovince']

    return cookies

# 获取账单时的 图形验证码
def get_project_verify_code_image(mobile,cookies):
    url = 'http://shop.10086.cn/i/authImg?t=' + str(random.random())
    response = requests.get(url,cookies=cookies)
    img = open(mobile + '2.jpg','wb+')
    img.write(response.content)
    img.close()
    print(response.status_code)

# 获取账单时 校验图形验证码
def get_project_verify_code(mobile,code,cookies):
    url = 'http://shop.10086.cn/i/v1/res/precheck/' + mobile + '?captchaVal=' + code + '&_=' + str(int(time.time()*1000))
    response = requests.get(url,cookies=cookies)
    result = json.loads(response.text)
    print('验证码是否正确  =>','正确' if result['retCode'] == '000000' else '错误')

# 获取账单时的 发送短信验证码
def get_project_send_code(mobile,cookies):
    url = 'https://shop.10086.cn/i/v1/fee/detbillrandomcodejsonp/' + mobile + '?callback=jQuery18307393072971157502_1512793409095&_=' + str(int(time.time()*1000))
    response = requests.get(url,cookies=cookies,verify=False)
    print(response.text)

# 获取账单时的 二次登陆
def get_project_login(mobile,code) :
    url = 'https://shop.10086.cn/i/v1/fee/detailbilltempidentjsonp/' + mobile + '?callback=jQuery18304613214506293093_1512798307557&pwdTempSerCode='+'MjYzNjYx'+'&pwdTempRandCode='+'MzE2MTE3'+'&captchaVal=' + code + '&_=' + str(int(time.time()*1000)) 
    response = requests.get(url)
    print()


# 账单接口
def detailbillinfojsonp(mobile,month):
    url = 'http://shop.10086.cn/i/v1/fee/detailbillinfojsonp/' + mobile + '?callback=jQuery18309695543543405936_1512465642278&curCuror=1&step=100&qryMonth=' + month + '&billType=02&_=' + str(int(time.time()*1000))
    response = requests.get(url)
    print(response.text)

mobile = '15011463580'
# chick_bj_mobile(mobile)
# send_code(mobile)
# code = input('code=')
# pwd = '263661'
# cookies = login(mobile,pwd,code)
# print(cookies)
cookies = {'is_login': 'true', 'userinfokey': '%7b%22loginType%22%3a%2201%22%2c%22provinceName%22%3a%22100%22%2c%22pwdType%22%3a%2201%22%7d', 'verifyCode': '4d7ce286a2e40576b33de45db42ab5db68209376', 'c': '4c18f34e87bc45b4adc2129a1800c303', 'jsessionid-echd-cpt-cmcc-jt': 'F9A8D74650C9D3B28254D261540041F9', 'ssologinprovince': '100'}

get_project_send_code(mobile,cookies)
get_project_verify_code_image(mobile,cookies)
imgCode = input('图形验证码是=')
get_project_verify_code(mobile,imgCode,cookies)


