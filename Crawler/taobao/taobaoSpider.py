# coding:utf-8

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq
from taobaoConfig import *
import pymongo

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

path = '/Users/y/Browser/chromedriver'
browser = webdriver.Chrome(path)
# path = '/Users/y/Browser/phantomjs'
# browser = webdriver.PhantomJS(path,service_args=SERVICE_ARGS)
# browser = webdriver.Safari()
wait = WebDriverWait(browser, 10)

def search():
    try:
        print('正在搜索')
        browser.get('https://www.taobao.com')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        input.send_keys('美食')
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total.text
    except TimeoutException as err:
        print('搜索出错，马上重试\n', err)
        return search()

def next_page(page_number):
    try:
        print('正在翻页',page_number)
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
        get_products()
    except TimeoutException as err:
        print('翻页出错，马上重试\n', err)
        next_page(page_number)

def get_products():
    print('正在解析')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR , '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.location').text(),
        }
        save_to_mongo(product)

def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('保存成功', result)
    except Exception as err:
        print('保存出错', result, '\n错误原因：', err)

def main():
    try:
        total = search()
        total = int(re.compile('(\d+)').search(total).group(1))
        for i in range(2, total+1):
            next_page(i)
    except Exception:
        print('出错了')
    finally:
        browser.close()

if '__main__' == __name__:
    main()