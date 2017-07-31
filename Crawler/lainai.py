#coding:utf-8

import requests
from bs4 import BeautifulSoup


class laonai():
    def __init__(self):
        self.headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

    def request(self,url):
        content = requests.get(url,headers=self.headers)
        return content.text

    def showData(self,context):
        f = open('f.txt','w+')
        all = BeautifulSoup(context,'lxml').find_all('div',class_='xinxi_righta')
        for index,item in enumerate(all):
            name = item.find('span',class_='zhen_name1')
            amount = item.find('span',class_='etention_xqxxaa')
            add = item.find_all('p')[1]
            haha = item.find_all('p')[0].find('b')
            ftxt = str(index) + '|' + name.get_text() + '|' + amount.get_text().strip() + '|' + add.get_text().strip()+ '|' + '危险等级:' + haha.get_text() + '\n'
            f.write(ftxt)
            print('姓名',name.get_text())
            print(amount.get_text().strip())
            print(add.get_text().strip())
            print('危险等级',haha.get_text())
            print('========',str)

Lao = laonai()
URL = 'http://www.thebetterchinese.com/show/lai.html?pageNo=1&pageSize=240'
text = Lao.request(URL)
Lao.showData(text)
