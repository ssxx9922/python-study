# -*- coding:utf-8  -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Safari()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.pp100.com")
        self.assertIn("壹佰金融", driver.title)
        elem = driver.find_element_by_name("")
        elem.send_keys("pp100")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()