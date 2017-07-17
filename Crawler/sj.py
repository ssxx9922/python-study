#coding:utf-8

import requests
from bs4 import BeautifulSoup
import time
# import pdb  #断点

class sj():

    def __init__(self):
        self.sjUrl = 'http://sj.pp100.net'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
        self.cookies = dict(cookies_are='gr_user_id=ffe2f418-5190-4108-aa21-55968dcc7d6c; _ga=GA1.2.1024082079.1498793915; phusr=shixiao; phsid=562b5yuhdhekbemldowyhl2z5du3txvfepw33gq2')
        self.task = []
        self.i = 0

    def mianHtml(self):
        
        html = requests.get(self.sjUrl, headers=self.headers,cookies = self.cookies)
        print('-----大家的任务-----')
        important = BeautifulSoup(html.text,'lxml').find_all('div',class_='phui-box phui-box-border mlt mll mlr phui-object-box')[0].find_all('div','phui-object-item-table-row')
        self.showList(important)
        print('------我的任务------')
        me = BeautifulSoup(html.text,'lxml').find_all('div',class_='phui-box phui-box-border mlt mll mlr phui-object-box')[2].find_all('ul','phui-object-item-list-view')
        self.showList(me)

    def showList(self,html):
        if len(html) == 0:
            print('没有任务')
        else:
            for a in html:
                title = a.find('span',class_='phui-object-item-objname')
                alink = a.find('a',class_='phui-object-item-link')
                atime = a.find('span',class_='phui-object-item-icon-label')
                timeTuple = time.strptime(atime.get_text(),'%a, %b %d, %I:%M %p')
                showtime = time.strftime("%m-%d %H:%M", timeTuple)
                name = a.find('a',class_='phui-handle phui-link-person')
                taskTitle = title.get_text()+ " " +alink.get_text()
                self.task.append(title.get_text())
                print('|',self.i ,'|',showtime,'|',taskTitle,'|',name.get_text(),'|')
                print('-----------------------------')
                self.i += 1

    def taskHtml(self,taskNum):
        task = self.task[taskNum]
        # pdb.set_trace()   #设置断点
        html = requests.get(self.sjUrl + '/' + task, headers=self.headers,cookies = self.cookies)
        beautiful = BeautifulSoup(html.text,'lxml')
        title = beautiful.find_all('div',class_='phabricator-remarkup')[0].get_text()
        print(title)

SJ = sj()
SJ.mianHtml()
a = input("task:")
SJ.taskHtml(int(a))



