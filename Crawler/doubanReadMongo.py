#coding:utf-8

import requests
import re
import pymongo
import time

class douban():
    def __init__(self):
        for i in range(1,1000,20):
            print('第',i,'页')
            url = self.getUrl(i)
            html = self.getRequest(url)
            print(html)
            self.readBook(html)
            time.sleep(4)

    def getRequest(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None

    def getUrl(self,page):
        url = "https://book.douban.com/tag/%E7%BB%8F%E6%B5%8E%E5%AD%A6?type=T&start=" + str(page)
        return url

    def readBook(self,html):
        regex = re.findall('<li class="subject-item.*?<a href="(.*?)" title="(.*?)".*?<div class="pub">(.*?)/.*?/(.*?)<.*?class="rating_nums">(.*?)<.*?',html,re.S)
        for result in regex:
            url = result[0]
            name = result[1].strip()
            author = result[2].strip()
            hahaha = result[3].strip()
            score = result[4].strip()
            
            hhh = hahaha.split('/')
            price = ''
            time = ''
            if len(hhh) > 1:    
                price = hhh[-1].strip()  # 价钱
                time = hhh[-2].strip()  # 时间
            press = ''
            if len(hhh) > 2:
                press = hhh[-3].strip()  # 出版社
            print('======')
            self.sqlInset(name,author,score,price,time,press,url)
            print('保存了',name)

    def sqlInset(self,name,author,score,price,time,press,url):
        try:
            conn = pymongo.MongoClient('mongodb://localhost:27017/')
            db = conn.douban
            book = db.book
            bo = {
                'name':name,
                'author':author,
                'score':score,
                'price':price,
                'time':time,
                'press':press,
                'url':url,
            }
            sb = book.find_one({'name':name})
            if sb == None:
                book.insert_one(bo)
                print('保存了',name)
            else:
                print(name,'已存在')
        except Exception as err:
            print(name,err)

db = douban()