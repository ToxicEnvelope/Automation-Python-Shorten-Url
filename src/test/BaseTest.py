#!/usr/bin/env python
from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BaseTest(object):

    BIN_PATH = '/Users/sysmurff/Desktop/GIT/BitlyAut/src/bin'
    CHROME_PATH = '{0}/chromedriver'.format(BIN_PATH)

    def setUp(self):
        # self.driver = webdriver.Remote(
        #     command_executor='http://localhost:4444/wd/hub',
        #     desired_capabilities=DesiredCapabilities.CHROME)
        self.driver = webdriver.Chrome(self.CHROME_PATH)

    def get_driver(self):
        return self.driver

    def tearDown(self):
        self.get_driver().close()
