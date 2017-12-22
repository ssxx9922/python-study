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

import re
import base64

result = 'jQuery18308124502347056595_1513071820224({"data":null,"retCode":"000000","retMsg":"success","sOperTime":null})'
s = re.search('({.*?})',result,re.S)
i = s.group()
print(json.loads(i)['retCode'])


print(base64.b64encode('079230'.encode('utf-8')).decode())

# ============================

GET /i/v1/fee/detailbillinfojsonp/15011463580?callback=jQuery1830615989468084053_1513759759587&curCuror=1&step=100&qryMonth=201711&billType=02&_=1513759888880 HTTP/1.1
Host: shop.10086.cn
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
Accept: */*
Referer: http://shop.10086.cn/i/?f=billdetailqry
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7
Cookie: ssologinprovince=100; collect_id=9pt9xruastbi31nir4wo5lvrwsvmo5ml; jsessionid-echd-cpt-cmcc-jt=90E57240A6482F0981F3E7027BF5B4A5; CmLocation=100|100; CmProvid=bj; cmccssotoken=f1640cbd8d6542ffa81cfa8a27d1d182@.10086.cn; is_login=true; userinfokey=%7b%22loginType%22%3a%2201%22%2c%22provinceName%22%3a%22100%22%2c%22pwdType%22%3a%2201%22%2c%22userName%22%3a%2215011463580%22%7d; c=f1640cbd8d6542ffa81cfa8a27d1d182; verifyCode=4d7ce286a2e40576b33de45db42ab5db68209376; WT_FPC=id=254f49c981fb5a23ab81513759453605:lv=1513759759682:ss=1513759453605


GET /i/v1/fee/detailbillinfojsonp/15011463580?callback=jQuery18309115520519448623_1513669304676&curCuror=1&step=100&qryMonth=201711&billType=02&_=1513761018418 HTTP/1.1
Host: shop.10086.cn
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
Referer: http://shop.10086.cn/i/?f=billdetailqry
Cookie: ssologinprovince=100; collect_id=9pt9xruastbi31nir4wo5lvrwsvmo5ml; jsessionid-echd-cpt-cmcc-jt=90E57240A6482F0981F3E7027BF5B4A5; CmLocation=100|100; CmProvid=bj; cmccssotoken=f1640cbd8d6542ffa81cfa8a27d1d182@.10086.cn; is_login=true; userinfokey=%7b%22loginType%22%3a%2201%22%2c%22provinceName%22%3a%22100%22%2c%22pwdType%22%3a%2201%22%2c%22userName%22%3a%2215011463580%22%7d; c=f1640cbd8d6542ffa81cfa8a27d1d182; verifyCode=4d7ce286a2e40576b33de45db42ab5db68209376; WT_FPC=id=254f49c981fb5a23ab81513759453605:lv=1513759759682:ss=1513759453605