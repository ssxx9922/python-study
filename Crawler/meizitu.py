#-*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import os


class mzitu():
    def all_url(self,url):
        html = self.request(url)
        all_a = BeautifulSoup(html.text,'lxml').find('div',class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存 ->  ',title)
            path = str(title).replace("?","_")
            self.mkdir(path)
            href = a['href']
            self.html(href)

    def html(self,href):
        html = self.request(href)
        if len(html.text) != 0:
            max_span = BeautifulSoup(html.text,'lxml').find('div',class_='pagenavi').find_all('span')[-2].get_text()
            for page in range(1, int(max_span)+1):
                page_url = href + '/' + str(page)
                self.img(page_url)

    def img(self,page_url): 
        img_html = self.request(page_url)
        if len(img_html.text) != 0:
            img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
            self.save(img_url)

    def save(self,img_url):
        name = img_url[-9:-4]
        img = self.request(img_url)
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
        isExists = os.path.exists(os.path.join('mzitu',path))
        if not isExists:
            print(u'创建了文件夹 ->  ',path)
            os.makedirs(os.path.join('D:\mzitu',path))
            os.chdir(os.path.join('D:\mzitu',path))
            return True
        else:
            print(path,u'文件夹已存在')
            return False

M = mzitu()
M.all_url('http://www.mzitu.com/all')
