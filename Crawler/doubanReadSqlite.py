#coding:utf-8

import requests
import re
import sqlite3


class douban():
    def __init__(self):
        # self.sqlInit()
        for i in range(0,1):
            print('第',i,'页')
            url = self.getUrl(i)
            html = self.getRequest(url)
            self.readBook(html.text)

    def getRequest(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
        response = requests.get(url, headers=headers)
        return response

    def getUrl(self,page):
        url = "https://book.douban.com/tag/%E7%BB%8F%E6%B5%8E%E5%AD%A6?type=T&start=" + str(page*20)
        return url

    def readBook(self,html):
        regex = re.findall('<li class="subject-item.*?<a href="(.*?)" title="(.*?)".*?<div class="pub">(.*?)/.*?/(.*?)<.*?class="rating_nums">(.*?)<.*?',html,re.S)
        for result in regex:
            url = result[0]
            name = result[1].strip()
            author = result[2].strip()
            price = result[3].strip()
            score = result[4].strip()
            
            hhh = price.split('/')
            print(price)
            print(hhh[-1])  # 价钱
            print(hhh[-2])  # 时间
            print(hhh[-3])  # 出版社
            print('======')
            # self.sqlInset(name,author,score,price,url)
            # print('保存了',name)

    def sqlInit(self):
        conn = sqlite3.connect('douban.db')
        cursor = conn.cursor()
        cursor.execute('create table book (id integer primary key autoincrement, name text(30),author text(30),price text(10), score text(10), url text(100))')
        cursor.close()
        conn.commit()
        conn.close()

    def sqlInset(self,name,author,score,price,url):
        conn = sqlite3.connect('douban.db')
        cursor = conn.cursor()
        sql = 'insert into book (name, author, score, price, url) values (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (name, author, score, price, url)
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

db = douban()