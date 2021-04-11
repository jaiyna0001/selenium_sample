#!/usr/local/bin/python3
import os
import sys
import datetime
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SELENIUM_HUB = 'http://selenium-hub:4444/wd/hub'

class SeleiumTests(unittest.TestCase):
    def test_title(self):
        self.driver.get('https://www.google.co.jp/')
        WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located)
        method_name = sys._getframe().f_code.co_name
        self.__screenshot(fname = method_name)
        self.assertTrue(self.driver.title == 'Google')

    def __screenshot(self, fname):
        dt = datetime.datetime.today()
        dtstr = dt.strftime("%Y%m%d%H%M%S")
        browser = self.driver.capabilities['browserName']
        self.driver.save_screenshot("images/%s/%s_%s.png" % (browser, fname, dtstr))

class ChromeTests(SeleiumTests):
    def setUp(self):
        self.driver = webdriver.Remote(
            desired_capabilities=DesiredCapabilities.CHROME,
            command_executor=SELENIUM_HUB
        )

class EdgeTests(SeleiumTests):
    def setUp(self):
        self.driver = webdriver.Remote(
            desired_capabilities=DesiredCapabilities.EDGE,
            command_executor=SELENIUM_HUB
        )

class FirefoxTests(SeleiumTests):
    def setUp(self):
        self.driver = webdriver.Remote(
            desired_capabilities=DesiredCapabilities.FIREFOX,
            command_executor=SELENIUM_HUB
        )

class OperaTests(SeleiumTests):
    def setUp(self):
        self.driver = webdriver.Remote(
            desired_capabilities=DesiredCapabilities.OPERA,
            command_executor=SELENIUM_HUB
        )

if __name__ == "__main__":
    TEST_LIST = [
        ChromeTests
        , FirefoxTests
        # , EdgeTests   #Edge is not work
        , OperaTests
    ]

    for test in TEST_LIST:
        suite = unittest.TestLoader().loadTestsFromTestCase(test)
        unittest.TextTestRunner(verbosity=3).run(suite)

