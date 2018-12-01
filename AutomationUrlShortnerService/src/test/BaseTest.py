#!/usr/bin/env python
import os
from selenium import webdriver


class BaseTest(object):

    BIN_PATH = '/Users/sysmurff/PycharmProjects/AutomationUrlShortnerService/src/bin'
    CHROME_PATH = '{0}/chromedriver'.format(BIN_PATH)


    def setUp(self):
        self.driver = webdriver.Chrome(self.CHROME_PATH)

    def get_driver(self):
        return self.driver

    def tearDown(self):
        self.get_driver().close()

    def open_new_tab(self, new_url):
        self.driver.execute_script('window.open('+new_url+', "_blank");')
