import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestBaiDu(unittest.TestCase):
    URL = "http://devbb-play.pp100.net/supervisor"


    def setUp(self):
        path = '/Users/pp/Browser/chromedriver'
        self.driver = webdriver.Safari()
        self.driver.implicitly_wait(30)     # 隐性等待，最长等30秒
        self.driver.get(self.URL)
        self.wait = WebDriverWait(self.driver, 10)

    def test_01(self):
        input0 = self.wait.until(EC.presence_of_element_located((By.ID, 'name')))
        input0.send_keys('supervisor')
        input1 = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        input1.send_keys('@pp100.com')     # 输入密码
        enter = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='安全登录']")))
        enter.click()     # 点击登录
        print('-----1')
        # total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "/html/body/div/div/div/div/div[2]/ul/li[1]/div[1]/span[1]")))
        time.sleep(5)
        print('-----2')
        print(self.driver)

        btn = self.driver.find_element_by_xpath("//*[@id='mg_3']/a")
        print('-----3')
        ActionChains(self.driver).move_to_element(btn).click().perform()
        print('-------end')
    def tearDown(self):
        # self.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main()