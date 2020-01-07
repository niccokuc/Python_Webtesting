'''
Created on 8 Jan. 2020

@author: NerminKuc
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import unittest
browser = webdriver.Firefox()

class TestStringMethods(unittest.TestCase):
    
    def test_getURL(self):
        browser.get("https://www.google.com/")
        first = browser.title
        print(first)
        self.assertEqual(first, "Google", "Does not equal")
        search_value = browser.find_element_by_name("q")
        search_value.send_keys("nermin kuc")
        sleep(3)
        browser.find_element_by_name("btnK").click()
        sleep(3)
        print(browser.title)
        assert browser.title == "nermin kuc - Google Search"
        browser.close()
        browser.quit()
                
if __name__ == '__main__':
    unittest.main()