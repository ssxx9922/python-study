#coding:utf-8

import requests
import time
import json
import random
import base64
import re
import math

def get_w():
    co_f='2'
    curt=str(int(time.time()*1000))
    for i in range(1,32-len(curt)):
	    co_f+=hex(math.floor(random.random()*16))[-1]
    co_f+=curt
    return 'id=' + co_f + ':lv=' + curt + ':ss=' + curt

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
    print('重定向之前的cookies =>',response.cookies)
    result = json.loads(response.text)
    cookies = {}
    cookies.update(response.cookies)
    # cookies['is_login'] = response.cookies['is_login']
    # cookies['userinfokey'] = response.cookies['userinfokey']
    # cookies['verifyCode'] = response.cookies['verifyCode']
    # cookies['c'] = response.cookies['c']
    newUrl = result['assertAcceptURL'] + '?backUrl=http://shop.10086.cn/i/sso.html&artifact=' + result['artifact']
    newResponse = requests.get(newUrl,cookies=cookies,verify=False,allow_redirects=False)
    print('重定向请求结果 =>',newResponse.status_code)
    print('重定向请求结果 =>',newResponse.cookies)
    # cookies['jsessionid-echd-cpt-cmcc-jt'] = newResponse.cookies['jsessionid-echd-cpt-cmcc-jt']
    # cookies['ssologinprovince'] = newResponse.cookies['ssologinprovince']
    # cookies['WT_FPC'] = get_w()
    # cookies['CmProvid'] = 'bj'
    # cookies['cmccssotoken'] = response.cookies['cmccssotoken']
    cookies.update(newResponse.cookies)
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
    print('验证码是否正确  =>','正确' if result['retCode'] == '000000' else '失败')

# 获取账单时的 发送短信验证码
def get_project_send_code(mobile,cookies):
    url = 'https://shop.10086.cn/i/v1/fee/detbillrandomcodejsonp/' + mobile + '?callback=jQuery18309115520519448623_1513669304676&_=' + str(int(time.time()*1000))
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Referer': 'http://shop.10086.cn/i/?f=billdetailqry'
    }
    response = requests.get(url,cookies=cookies,headers=headers,verify=False)
    print(response.status_code)
    print(response.text)
    jsonStr = re.search('({.*?})',response.text,re.S).group()
    result = json.loads(jsonStr)
    print('发送验证码是否正确  =>','正确' if result['retCode'] == '000000' else '失败')


# 获取账单时的 二次登陆
def get_project_login(mobile,pwd,smsCode,imgCode,cookies):
    url = 'https://shop.10086.cn/i/v1/fee/detailbilltempidentjsonp/{mobile}?callback=jQuery18309115520519448623_1513669304676&pwdTempSerCode={pwd}&pwdTempRandCode={smsCode}&captchaVal={imgCode}&_={timeStr}'
    url = url.format(mobile=mobile,pwd=base64.b64encode(pwd.encode(encoding='utf-8')).decode(),smsCode=base64.b64encode(smsCode.encode(encoding='utf-8')).decode(),imgCode=imgCode,timeStr=str(int(time.time()*1000)))
    # data = {
    #     'callback':'jQuery18309115520519448623_1513669304676',
    #     'pwdTempSerCode':base64.b64encode(pwd.encode(encoding='utf-8')).decode(),#服务密码
    #     'pwdTempRandCode':base64.b64encode(smsCode.encode(encoding='utf-8')).decode(),#短信验证码
    #     'captchaVal':imgCode,#图形验证码
    #     '_':str(int(time.time()*1000))
    # }
    headers = {
        'Referer':'http://shop.10086.cn/i/?f=billdetailqry',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    response = requests.get(url,headers=headers,cookies=cookies,verify=False)
    print('二次登录')
    print(response.status_code)
    print(response.text)
    print(response.cookies)
    jsonStr = re.search('({.*?})',response.text,re.S).group()
    result = json.loads(jsonStr)
    print('登录是否成功  =>','正确' if result['retCode'] == '000000' else '失败')


# 账单接口
def detailbillinfojsonp(mobile,month,billType,cookies):
    url = 'https://shop.10086.cn/i/v1/fee/detailbillinfojsonp/{mobile}?callback=jQuery1830615989468084053_1513759759587&curCuror=1&step=100&qryMonth={month}&billType={type}&_={timeStr}'
    url = url.format(mobile=mobile,month=month,type=billType,timeStr=str(int(time.time()*1000)))
    # data = {
    #     'callback':'jQuery18309115520519448623_1513669304676',
    #     'curCuror':'1',
    #     'step':'100',
    #     'qryMonth':month, # 201711
    #     'billType':'02', # 01 套餐及固话 04上网 02 通话 03 短彩信 05增值业务
    #     '_':str(int(time.time()*1000))
    # }
    headers = {
        'Referer':'http://shop.10086.cn/i/?f=billdetailqry',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }
    response = requests.get(url,headers=headers,cookies=cookies,verify=False)
    print(response.status_code)
    print(response.text)

def get_basic(mobile,cookies):
    url = 'http://shop.10086.cn/i/v1/cust/info/' + mobile + '?_=' + str(int(time.time()*1000))
    headers = {
        'Referer':'http://shop.10086.cn/i/?f=billdetailqry',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    response = requests.get(url,headers=headers,cookies=cookies)
    result = json.loads(response.text)
    print(result['data'])

mobile = '15730495775'
pwd = '518099'

chick_bj_mobile(mobile)
send_code(mobile)
code = input('code=')
cookies = login(mobile,pwd,code)
cookies['WT_FPC'] = get_w()
print('第一次cookies =>',cookies)

# cookies = {'CmLocation': '230|230', 'CmProvid': 'cq', 'c': 'b8e4be6cc3a14ea6a83f8cdc335f10e1', 'cmccssotoken': 'b8e4be6cc3a14ea6a83f8cdc335f10e1@.10086.cn', 'is_login': 'true', 'userinfokey': '%7b%22loginType%22%3a%2201%22%2c%22provinceName%22%3a%22230%22%2c%22pwdType%22%3a%2201%22%2c%22userName%22%3a%2215730495775%22%7d', 'verifyCode': '6c135c30f8b88c7d969e207b9ed5dfdd77ef0944', 'jsessionid-echd-cpt-cmcc-jt': '6A64A109C1C557742333613FFAAB6D44', 'ssologinprovince': '230', 'WT_FPC': 'id=221b7b0ea94bfd34ce01513755626799:lv=1513755626799:ss=1513755626799'}
# 'CmLocation': '230|230', 'CmProvid': 'cq',
# print(cookies)

# time.sleep(10)


get_project_send_code(mobile,cookies)
get_project_verify_code_image(mobile,cookies)
imgCode = input('图形验证码是=')
get_project_verify_code(mobile,imgCode,cookies)
while(True):
    smsCode = input('短信验证码是=')
    next = input('是否下一步 [y/n] =>')
    if next == 'y':
        get_project_login(mobile,pwd,smsCode,imgCode,cookies)
    elif next == 'n':
        get_project_send_code(mobile,cookies)
    elif next == 'e':
        break

get_basic(mobile,cookies)
detailbillinfojsonp(mobile,'201711','02',cookies)
detailbillinfojsonp(mobile,'201710','02',cookies)
detailbillinfojsonp(mobile,'201711','03',cookies)
detailbillinfojsonp(mobile,'201710','03',cookies)


