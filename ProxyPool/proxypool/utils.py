import requests
import asyncio
import aiohttp
from requests.exceptions import ConnectionError
import random



def get_page(url, options={}):
    ua = UserAgent()
    base_headers = {
        'User-Agent': ua.random,
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    headers = dict(base_headers, **options)
    print('Getting', url)
    try:
        r = requests.get(url, headers=headers)
        print('Getting result', url, r.status_code)
        if r.status_code == 200:
            return t.text
    except ConnectionError:
        print('Crawling Failed', url)
        return None

