#coding:utf-8

import requests
from lxml import etree

class sj():

    def __init__(self):
        self.sjUrl = 'http://sj.pp100.net'
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        self.cookie = []

    def login(self,username,password):
        print('准备登录')
        response = requests.get(self.sjUrl)
        html = etree.HTML(response.text)
        scrfValue = html.xpath('//*[@id="UQ0_0"]/form/input[1]')[0].get('value')
        self.cookie = response.cookies

        print('开始登录')
        parme = {'__csrf__':scrfValue,'__form__':'1','__dialog__':'1','username':username,'password':password}
        session = requests.session()
        session.post(url="http://sj.pp100.net/auth/login/password:self/",headers=self.header,cookies=self.cookie,data=parme)
        if session.cookies is not None:
            print('登录成功')
            self.cookie = session.cookies
            print(self.cookie)


    def get_home(self):
        response = requests.get(self.sjUrl,headers=self.header,cookies=self.cookie)
        html = etree.HTML(response.text)
        list = html.xpath('//*[@id="UQ0_0"]/div[1]/div[3]/ul/li')
        print(list)
        for item in list:
            task = item.xpath('./div/div/div/div/div[2]/div[1]/a')
            title = task[0].get('href')
            href = task[0].get('title')
            print('=>',task)
            print(title)
            print(href)

    def get_info(self,href):
        url = self.sjUrl+'/'+href
        response = requests.get(url,cookies=self.cookie,headers=self.header)
        html = etree.HTML(response.text)
        scrfValue = html.xpath('//*[@id="UQ0_9"]/ul[2]/li/div/form/input[1]')



s = sj()
 username = input('username:')
 password = input('password:')
s.login(username,password)
s.get_home()

# ,allow_redirects=False
