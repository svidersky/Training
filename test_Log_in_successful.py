#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(implicitly_wait)
        self.base_url = bmp_url
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Пресса").click()
        driver.find_element_by_link_text("RU").click()
        driver.find_element_by_link_text("EN").click()
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_id("login_login").clear()
        driver.find_element_by_id("login_login").send_keys("0000")
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("0000")
        driver.find_element_by_css_selector("#login > a.button.blue").click()
        try: self.assertEqual("0000", driver.find_element_by_link_text("0000").text)
        except AssertionError as e: self.verificationErrors.append(str(e))  
   
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
