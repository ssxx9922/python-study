#coding:utf-8

import requests


newurl = 'http://bj.ac.10086.cn/ac/cmsso/redirect.jsp'
# headers = {
# 	'Host':'bj.ac.10086.cn',
# 	'Connection':'keep-alive',
# 	'Content-Length':'285',
# 	'Cache-Control':'max-age=0',
# 	'Origin':'https://bj.ac.10086.cn',
# 	'Upgrade-Insecure-Requests':'1',
# 	'Content-Type':'application/x-www-form-urlencoded',
# 	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
# 	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 	'Referer':'https://bj.ac.10086.cn/ac/cmsso/iloginnew.jsp',
# 	'Accept-Encoding':'gzip, deflate, br',
# 	'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
# }

response = requests.get(newurl, allow_redirects=False)

print('北京移动，登录第二步：', response.status_code, response.headers)