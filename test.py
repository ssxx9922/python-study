# coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


path = '/Users/yy/PY/chromedriver/chromedriver'
browser = webdriver.Chrome(path)
# path = '/Users/yy/PY/phantomjs-2.1.1-macosx/bin/phantomjs'
# browser = webdriver.PhantomJS(path)

wait = WebDriverWait(browser, 10)


def login():
    try:
        print('logining...')
        browser.get('http://sj.pp100.net')
        inputName = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#UQ0_2'))
        )
        inputPwd = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#UQ0_3'))
        )
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#UQ0_0 > form > div.aphront-dialog-tail.grouped > button')))
        inputName.send_keys('shixiao')
        inputPwd.send_keys('sxxhyl1992')
        submit.click()
    except TimeoutException as err:
        print('login error')
        return login()

def main():
    try:
        login()
    except Exception:
        print('出错了')
    finally:
        browser.close()

if '__main__' == __name__:
    main()

