#coding:utf-8

import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool
import time

def get_one_page(url):
    try:
        hearder = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
        response = requests.get(url)
        print(url," -->  ",response.status_code)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">'
                         +'<a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?inte'
                         +'ger">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5],
            'score':item[5]+item[6],
        }

def wrtie_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    print(url)
    html = get_one_page(url)
    print(html)
    for item in parse_one_page(html):
        print(item)
        wrtie_to_file(item)

                         
if __name__ == '__main__':
    # pool = Pool()
    # pool.map(main,[i*10 for i in range(10)])
    # pool.close()
    # pool.join()
    # main(0)
    for i in range(0,90,10):
        main(i)
        time.sleep(1)