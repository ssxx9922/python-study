#-*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
from Download import request
import os
from pymongo import MongoClient
import datetime

class mzitu():

    def __init__(self):
        client = MongoClient()
        db = client['meinvxiezhengji']
        self.meizitu_collection = db['meizitu']
        self.title = ''
        self.url = ''
        self.img_urls = []

    def all_url(self,url):
        html = request.get(url,3)
        all_a = BeautifulSoup(html.text,'lxml').find('div',class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存 ->  ',title)
            path = str(title).replace("?","_")
            self.mkdir(path)
            href = a['href']
            self.url = href
            os.chdir('/Users/pp/Demo/python-study/Crawler/mzitu/' + path)
            if self.meizitu_collection.find_one({'主题页面':href}):
                print(href,'已经存在了')
            else:
                self.html(href)

    def html(self,href):
        html = request.get(href,3)
        if len(html.text) != 0:
            max_span = BeautifulSoup(html.text,'lxml').find('div',class_='pagenavi').find_all('span')[-2].get_text()
            page_num = 0
            for page in range(1, int(max_span)+1):
                page_num += 1

                page_url = href + '/' + str(page)
                self.img(page_url,max_span,page_num)

    def img(self,page_url,max_span,page_num): 
        img_html = request.get(page_url,3)
        if len(img_html.text) != 0:
            img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
            self.img_urls.append(img_url)
            print('最大值',max_span,'   |   当前值',page_num)
            if int(max_span) == page_num:
                self.save(img_url)
                post = {
                    '标题':self.title,
                    '主题页面':self.url,
                    '图片地址':self.img_urls,
                    '获取时间':datetime.datetime.now()
                }
                self.meizitu_collection.save(post)
                print('获取的图片信息插入数据库')
            else:
                self.save(img_url)

    def save(self,img_url):
        name = img_url[-9:-4]
        img = request.get(img_url,3)
        print(u'写入文件 ->  ',name)
        f = open(name+'.jpg','ab')
        f.write(img.content)
        f.close()

    def request(self,url):
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url,headers=headers)
        return content

    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(os.path.join('/Users/pp/Demo/python-study/Crawler/mzitu',path))
        if not isExists:
            print(u'创建了文件夹 ->  ',path)
            os.makedirs(os.path.join('/Users/pp/Demo/python-study/Crawler/mzitu',path))
            os.chdir(os.path.join('/Users/pp/Demo/python-study/Crawler/mzitu',path))
            return True
        else:
            print(path,u'文件夹已存在')
            return False

M = mzitu()
M.all_url('http://www.mzitu.com/all')
