#coding:utf-8

import requests
import os

imgURL='http://login.189.cn/web/login/ajax'
cookieStr=' code_v=20170913; __qc_wId=567; svid=68D53DACA94EFB9B; pgv_pvid=246305230; code_v=20170913; lvid=1732e478edefed467924daeca27047d3; nvid=1; EcsCaptchaKey=OHPlRbpTaMUh%2F5dzpmO4Tk7ihfDGg9rSiJ6aNlbkY8w6vi5AM3%2Bqfg%3D%3D; ECS_ReqInfo_login1=U2FsdGVkX19tEm44F6OdHcUtaAIORoBpmj8lAZ2VZ%2BA1qu1pwmW40y6TwpiyX4J124%2F%2BnzXPj3uyLYuLbUY2cnL2YV4Wue7CJpviH4LwyZE%3D; trkHmClickCoords=768%2C457%2C684; s_cc=true; s_fid=296B1311573D8571-02140C49EBF82F73; loginStatus=non-logined; trkId=27E6818E-1078-4BA5-A329-F57B29B75447'

cookie={}
for item in cookieStr.split(';'):
    name,value=item.strip().split('=',1)
    cookie[name]=value
img = requests.post(imgURL,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'},cookies=cookie)

print(img.text)

f = open('code.jpg','ab')
f.write(img.content)
f.close()