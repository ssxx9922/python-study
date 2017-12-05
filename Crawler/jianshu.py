#coding:utf-8
import requests
from bs4 import BeautifulSoup

def get_list(user):
    user_url = 'http://www.jianshu.com/u/{user}?order_by=shared_at&page={page}'
    for i in range(1,48):
        response = requests.get(user_url.format(user=user,page=str(i)))
        result = BeautifulSoup(response.text,'lxml').find_all('a',class_='title')
        titleList = []
        for title in result:
            print(title['href'])
            titleList.append(title['href'])
        write_file(titleList)

def write_file(url_list):
    
    for url in url_list:
        url = 'http://www.jianshu.com'+url
        response = requests.get(url)
        result = BeautifulSoup(response.text,'lxml')
        title = result.find('title').get_text()
        wrtie_to_file('## ' + title)
        wrtie_to_file('原文链接:' + url)
        print(title)
        text = result.find('div',class_='show-content')
        wrtie_to_file('=====')
        wrtie_to_file(str(text))
        wrtie_to_file('=====')

def wrtie_to_file(content):
    with open('chunyin.md', 'a', encoding='utf-8') as f:
        f.write(content + '\n')
        f.close()


get_list('c22ccc510fb9')
