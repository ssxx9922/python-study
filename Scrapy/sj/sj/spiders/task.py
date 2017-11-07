# -*- coding: utf-8 -*-
import scrapy
from sj.items import SjItem


class TaskSpider(scrapy.Spider):
    name = 'task'
    allowed_domains = ['sj.pp100.net']
    cookie = {'phusr':'shixiao', 'phsid':'a5txe74h56lj2amthfvetudidphamiz2vxaukxyx'}

    def start_requests(self):
        # cookie = {'phusr':'shixiao', 'phsid':'a5txe74h56lj2amthfvetudidphamiz2vxaukxyx'}
        for i in range(10000,11500):
            url = self.getUrl(i)
            yield scrapy.Request(url=url, cookies=TaskSpider.cookie, callback=self.parse)
            
    def getUrl(self,num):
        return 'http://sj.pp100.net/T' + str(num)

    def parse(self, response):
        # print(response.body)
        # self.getInfo(response.body,response.url)
        print('>>>>>>>>>>>>')
        title = response.xpath('//*[@id="UQ0_1"]/div[2]/div[1]/h1/div/div[1]/span/text()').extract_first()

        status = response.xpath('//*[@id="UQ0_1"]/div[2]/div[1]/h1/div/div[1]/div/span[1]/text()').extract_first()

        people = response.xpath('//*[@id="UQ0_1"]/div[2]/div[1]/h1/div/div[1]/div/span[2]/a/text()').extract_first()

        toUser = response.xpath('//*[@id="UQ0_1"]/div[2]/div[2]/div[1]/div/div[2]/dl/dd[1]/a/text()').extract()

        priopity = response.xpath('//*[@id="UQ0_1"]/div[2]/div[2]/div[1]/div/div[2]/dl/dd[2]/text()').extract_first()

        fromUser = response.xpath('//*[@id="UQ0_1"]/div[2]/div[2]/div[1]/div/div[2]/dl/dd[3]/a/text()').extract()

        product = response.xpath('//*[@id="UQ0_1"]/div[2]/div[2]/div[1]/div/div[2]/dl/dd[4]/span/a/text()').extract_first()

        lookUser = response.xpath('//*[@id="UQ0_1"]/div[2]/div[2]/div[1]/div/div[2]/dl/dd[5]/a/text()').extract()

        item = SjItem()
        item['title'] = title
        item['status'] = status
        item['people'] = people
        item['toUser'] = toUser
        item['priopity'] = priopity
        item['fromUser'] = fromUser
        item['lookUser'] = lookUser
        item['product'] = product

        url = response.url
        num = url.split('T')[1]
        item['taskId'] = 'T' + num
        yield item
        # nextUrl = self.getUrl(int(num))
        # print('>>>',num,title)
        # yield scrapy.Request(url=nextUrl, cookies=TaskSpider.cookie, callback=self.parse)
