# -*- coding:utf-8  -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        path = '/Users/pp/chromedriver'
        self.driver = webdriver.Chrome(path)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.baidu.com")
        self.assertIn("百度一下", driver.title)
        elem = driver.find_element_by_id("kw")
        elem.send_keys("pp100")
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()