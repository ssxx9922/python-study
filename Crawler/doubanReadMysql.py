#coding:utf-8

import requests
import re
import pymysql


class douban():
    def __init__(self):
        # self.sqlInit()
        for i in range(0,50):
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
            # price = result[3].strip()
            score = result[4].strip()
            self.sqlInset(name,author,score,url)

    def sqlInit(self):
        db = pymysql.connect(host='localhost', user='root', password='password', port=3306, db='spiders')
        cursor = db.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS book (id INT NOT NULL AUTO_INCREMENT, name TEXT NOT NULL, author TEXT NOT NULL, score FLOAT NOT NULL, url TEXT NOT NULL, PRIMARY KEY (id))'
        cursor.execute(sql)
        db.close()

    def sqlInset(self,name,author,score,url):
        db = pymysql.connect(host='localhost', user='root', password='password', port=3306, db='spiders')
        cursor = db.cursor()
        sql = 'INSERT INTO book(name, author, score, url) values(%s, %s, %s, %s)'
        try:
            cursor.execute(sql, (name.encode('utf-8'), author.encode('utf-8'), score.encode('utf-8'), url.encode('utf-8')))
            db.commit()
            print('保存了',name)
        except Exception as err:
            print(err)
            db.rollback()
            print('未保存',name)
        db.close()

db = douban()