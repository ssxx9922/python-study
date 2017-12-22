# -*- coding: utf-8 -*-
from scrapy import  Spider, FormRequest

class WeiboSpider(Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    start_urls = ['http://weibo.cn/']
    search_url = 'http://weibo.cn/search/mblog'
    max_page = 100

    def start_requests(self):
        keyword = '000001'
        for page in range(self.max_page + 1):
            url = '{url}?hideSearchFrame=&keyword={keyword}&page={page}'.format(url=self.search_url, keyword=keyword,page=page)
            yield FormRequest(url, callback=self.parse_index)

    def parse_index(self, response):
        print(response.text)
