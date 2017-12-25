#coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import requests
import os


import time

path = '/Users/y/Browser/chromedriver'
browser = webdriver.Chrome(path)

wait = WebDriverWait(browser, 10)


def openBrowser():
    try:
        print('打开浏览器')
        browser.get('http://login.189.cn/login')
        inputMobile = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#txtAccount'))
        )
        inputMobile.send_keys('18050055118')

        js = "document.getElementById('txtPassword').style.display='block';"
        browser.execute_script(js)
        # inputPwdDiv = browser.find_element_by_css_selector('#txtShowPwd')
        # inputPwdDiv.
        # ActionChains(browser).move_to_element(inputPwdDiv).click(inputPwdDiv).perform()
        inputPwd = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#txtPassword'))
        )
        inputPwd.send_keys('518316')

        codeImage = browser.find_element_by_css_selector('#imgCaptcha').get_attribute('src')
        print(codeImage)

        print(browser.get_cookies())
        print('============')
        for item in browser.get_cookies():
            print(item)

    except TimeoutException as err:
        print('登录出错')

def main():
    openBrowser()

if '__main__' == __name__:
    main()

