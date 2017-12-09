#coding:utf-8

import requests
import time
import json
# cookies = {}
# cookies['is_login'] = 'true'
# cookies['userinfokey'] = '%7b%22loginType%22%3a%2201%22%2c%22provinceName%22%3a%22100%22%2c%22pwdType%22%3a%2201%22%7d'
# cookies['verifyCode'] = '4d7ce286a2e40576b33de45db42ab5db68209376'
# cookies['c'] = '4c18f34e87bc45b4adc2129a1800c303'
# newUrl = 'http://shop.10086.cn/i/v1/auth/getArtifact' + '?backUrl=http://shop.10086.cn/i/sso.html&artifact=a257b26a5ad0436ba82d212083ad585e'
# newResponse = requests.get(newUrl,cookies=cookies,verify=False,allow_redirects=False)
# print(newResponse.cookies)
# cookies['jsessionid-echd-cpt-cmcc-jt'] = newResponse.cookies['jsessionid-echd-cpt-cmcc-jt']
# cookies['ssologinprovince'] = newResponse.cookies['ssologinprovince']
# print(cookies)

cookies = {'is_login': 'true', 'userinfokey': '%7b%22loginType%22%3a%2201%22%2c%22provinceName%22%3a%22100%22%2c%22pwdType%22%3a%2201%22%7d', 'verifyCode': '4d7ce286a2e40576b33de45db42ab5db68209376', 'c': '4c18f34e87bc45b4adc2129a1800c303', 'jsessionid-echd-cpt-cmcc-jt': 'F9A8D74650C9D3B28254D261540041F9', 'ssologinprovince': '100'}
print(type(cookies))
print(cookies)