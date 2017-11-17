#coding:utf-8

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import os


# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chrome_options.add_experimental_option("prefs",prefs)
            
# path = '/Users/yy/PY/chromedriver/chromedriver'
# browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
browser = webdriver.Safari()

mobile = '18050055118'
pwd = '518317'

wait = WebDriverWait(browser,10)

def openLogin():
    try:
        print('打开登录页')
        url = 'http://login.189.cn'
        browser.get(url)
        inputMobile=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#txtAccount'))
        )
        inputMobile.send_keys(mobile)
        browser.execute_script("document.getElementById('txtPassword').style.display='block'")
        inpotPwd=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#txtPassword'))
        )
        inpotPwd.send_keys(pwd)

        imgUrl = browser.find_element_by_css_selector('#imgCaptcha').get_attribute('src')
        print(imgUrl)
        print('==========')

        cookiedict = {}
        for cookie in browser.get_cookies():
            cookiedict[cookie['name']] = cookie['value']
        
        print(cookie)
        print('==========')
        downloadImage(imgUrl,cookiedict,'1')

        code = input("验证码:")
        
        inpotCode=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#txtCaptcha'))
        )
        inpotCode.send_keys(code)

        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginbtn')))
        submit.click()

    except TimeoutException as err:
        print('打开网页出错',err)

def openBrowser():
    try:
        print('打开网页')
        url = 'http://uam.ct10000.com/ct10000uam/login?service=https%3A%2F%2Fuam.ct10000.com%3A443%2Fct10000uam-gate%2FSSOFromUAM%3FReturnURL%3D687474703A2F2F67642E3138392E636E2F736572766963652F686F6D652F71756572792F78645F696E6465782E68746D6C3F696E5F636D7069643D676464732D746F702D77647864%26ProvinceId%3D20&serviceId=001&ProvinceId=20'
        browser.get(url)
        inputMobile=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#username'))
        )
        inputMobile.send_keys('18050055118')
        inpotPwd=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#password'))
        )
        inpotPwd.send_keys('518316')

        imgUrl = browser.find_element_by_css_selector('#checkImg').get_attribute('src')
        print(imgUrl)
        print('==========')
        

        
        # print(browser.get_cookie())
        cookie = {}
        for i in browser.get_cookies():
            cookie[i['name']]=i['value']

        downloadImage(imgUrl,cookie,'2')


        
    except TimeoutException as err:
        print('打开网页出错',err)

def downloadImage(url,cookie,name):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
    response = requests.get(url,cookies=cookie,headers=headers)
    img = open(name + '.jpg','wb+')
    img.write(response.content)
    img.close()

def main():
    openLogin()

if '__main__'==__name__:
    main()

