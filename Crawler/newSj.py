#coding:utf-8

from selenium import webdriver
from  selenium.webdriver.common.keys import Keys

path = '/Users/pp/Downloads/chromedriver'
driver = webdriver.Chrome(path)
driver.get('http://sj.pp100.net')
elem = driver.find_element_by_id("UQ0_2")
elem.send_keys("shixiao")
elem = driver.find_element_by_id("UQ0_3")
elem.send_keys("sxxhyl1992")
elem.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
print(driver.get_cookies())

