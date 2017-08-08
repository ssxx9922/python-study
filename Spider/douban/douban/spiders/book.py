# coding:utf-8

import scrapy
from bs4 import BeautifulSoup
import pymongo
import re


class BookSqider(scrapy.Spider):
    name = 'book'  # 标识爬虫。它在项目中必须是唯一的，也就是说，您不能为不同的Spider设置相同的名称。

    def start_requests(
            self
    ):  # 必须返回一个迭代的Requests（你可以返回请求列表或写一个生成器函数），Spider将开始抓取。后续请求将从这些初始请求连续生成。
        # urls = [
        #     'https://book.douban.com/subject/1000001/'
        # ]
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'
        }
        for url in self.urls():
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def urls(self):
        urlList = []
        for i in range(667, 100000):
            l = 1000000 + i
            url = 'https://book.douban.com/subject/%s/' % (l)
            urlList.append(url)
        return urlList

    def parse(self, response):  # 将被调用来处理为每个请求下载的响应的方法。response参数是一个TextResponse保存页面内容的实例，并且具有更多有用的方法来处理它。
        html = BeautifulSoup(response.body, 'lxml')

        title = html.find('div', id='wrapper').find('h1').get_text().strip()
        print(title)
        info = html.find('div', id='info')

        con = re.sub('<a.*?>|</a>', '', str(info))

        con1 = re.sub('</span>', '', con)

        con2 = re.sub('\s', '', con1)

        results = re.findall('<spanc.*?>(.*?):(.*?)<b.*?>', con2, re.S)

        dic = {}
        for result in results:
            key = result[0]
            value = result[1]
            dic[key] = value

        scoreh = html.find('strong', class_='ll rating_num ')
        score1 = scoreh.get_text().strip()
        score = 0 if not score1 else float(score1)

        try:
            peopleh = html.find('a', class_='rating_people').find('span')
            people1 = peopleh.get_text()
            people = 0 if not people1 else int(people1)
        except Exception:
            people = 0

        tags = html.find_all('a', class_='tag')

        tagList = []
        for tag in tags:
            tagList.append(tag.get_text())

        try:
            intro = html.find('div', class_='intro').find('p').get_text().strip()
        except Exception:
            intro = ''

        bookdata = {
            'url': response.url,
            'name': title,
            'results': dic,
            'score': score,
            'people': people,
            'tags': tagList,
            'intro': intro
        }
        print('要保存的数据为', bookdata)
        self.sqlInset(bookdata)


    def sqlInset(self, bookData):
        try:
            conn = pymongo.MongoClient('mongodb://localhost:27017/')
            db = conn.douban
            book = db.bookAll
            sb = book.find_one({'url': bookData['url']})
            if not sb:
                book.insert_one(bookData)
                print('success save', bookData['url'])
            else:
                print(bookData['url'], 'is have')
        except Exception as err:
            print(bookData['url'], 'eeeeeeeeeee error is ', err)
