import requests
import dianxin1

def login(mobile,pwd,code,cookies):
    login_url = 'http://login.189.cn/web/login'
    headers = {'Host':'login.189.cn',
        'Cache-Control':'max-age=0',
        'Origin':'http://login.189.cn',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer':'http://login.189.cn/login',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
        'Content-Length':'125',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':cookies}

    body = {'AreaCode':'','CityNo':'','Account':mobile,'UType':'201','ProvinceID':'14','RandomFlag':'0','Password':pwd,'Captcha':code}
    print(body)
    response = requests.post(login_url,headers=headers,data=body,allow_redirects=False)
    print(response.status_code)
    print(response.headers)
    id_url = response.headers['Location']

    response = requests.get(id_url,allow_redirects=False)
    print(response.status_code)
    print(response.headers['Set-Cookie'])


login('18050055118','0uPemJpAdhN40Sj97vogmg==','rw4n','__qc_wId=119; pgv_pvid=3095951590; EcsCaptchaKey=mZg8aWaXiKYSnFewnKDwzzDGswdKEY2BklC2mhmeJaf46%2BBm%2Bo2o0Q%3D%3D; ECS_ReqInfo_login1=U2FsdGVkX19dNvyqLHDT4MoLv3LyuvBJrTi9E6hNzaZQMCyx3WzYrMCXQwwr8%2BmqrK7d5lLQrnRl3JmyJEUpOtpZsxnIuMyy3FKiVYYzSn8%3D')