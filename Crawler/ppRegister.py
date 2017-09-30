#coding:utf-8

from selenium import webdriver

path = '/Users/pp/chromedriver'
browser = webdriver.Chrome(path)
browser.get('http://www.taobao.com')
print(browser.page_source)
browser.close()