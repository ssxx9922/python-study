#coding:utf-8

import requests
from bs4 import BeautifulSoup
import time
import pymongo

class sj():

    def __init__(self):
        self.sjUrl = 'http://sj.pp100.net/T1099'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
        self.cookies = dict(cookies_are='gr_user_id=ffe2f418-5190-4108-aa21-55968dcc7d6c; _ga=GA1.2.1024082079.1498793915; phusr=shixiao; phsid=562b5yuhdhekbemldowyhl2z5du3txvfepw33gq2')

    def getHtml(self,url):
        try:
            response = requests.get(url,headers=self.headers,cookies = self.cookies)
            if response.status_code == 200:
                return response.text
            return None
        except :
            print(url,'->出错了')
            return None

    def getInfo(self,html,name):

        try:
            bs = BeautifulSoup(html,'lxml')
        except:
            print('bs error')

        try:
            bs1 = bs.find('div',class_='phui-header-col2')
            title = bs1.find('span',class_='phui-header-header').get_text()
            status = bs1.find('span',class_='phui-header-status phui-header-status-dark').get_text()
            people = bs1.find('a',class_='policy-link').get_text()
        except:
            title = ''
            status = ''
            people = ''
            print(name,'bs1 error')

        try:
            bs2 = bs.find('div',class_='phui-property-list-properties-wrap ').find_all('dd',class_='phui-property-list-value')
            toUser = bs2[0].get_text()
            priopity = bs2[1].get_text()
            fromUser = bs2[2].get_text()
            lookUser = bs2[3].get_text()
            product = bs2[4].get_text()
        except:
            toUser = ''
            priopity = ''
            fromUser = ''
            lookUser = ''
            product = ''
            print(name,'bs2 error')
        
        try:
            info = bs.find('div',class_='phabricator-remarkup').get_text()
        except:
            info = ''
            print(name,'info error')

        self.saveData(name,title,status,people,toUser,priopity,fromUser,lookUser,product,info)

    def saveData(self,name,title,status,people,toUser,priopity,fromUser,lookUser,product,info):
        try:
            conn = pymongo.MongoClient('mongodb://localhost:27017/')
            db = conn.sj
            task = db.task
            data = {
                'name':name,
                'title':title,
                'status':status,
                'people':people,
                'toUser':toUser,
                'priopity':priopity,
                'fromUser':fromUser,
                'lookUser':lookUser,
                'product':product,
                'info':info,
            }
            taskName = task.find_one({'name':name})
            if taskName == None:
                task.insert_one(data)
                print('保存了',name)
            else:
                print(name,'已存在')
        except Exception as err:
            print(name,err)

    def getUrl(self):
        for i in range(9970,11000):
            url = 'http://sj.pp100.net/T' + str(i)
            html = self.getHtml(url)
            self.getInfo(html,'T' + str(i))

s = sj()
s.getUrl()