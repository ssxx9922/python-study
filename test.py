#coding:utf-8
from selenium import webdriver

browser = webdriver.Safari()
browser.get('https://www.baidu.com')
print(browser.page_source)
browser.close()
