#!/usr/bin/env python
from selenium import webdriver
from src.main.base.utils.Logger import Logger
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BaseTest(object):

    log = Logger()

    BIN_PATH = '/Users/sysmurff/Desktop/GIT/BitlyAut/src/bin'
    CHROME_PATH = '{0}/chromedriver'.format(BIN_PATH)
    """
        [Description]
        setUp
        :param -> dockerized : Boolean
        - This method responsible of starting up the browser process.
          If `dockerized=True` then docker session will take place,
          Otherwise local session will take place.
    """
    def setUp(self, dockerized=True):
        self.log.info('[BaseTest - Call "setUp" -> is_docker {0}]'.format(dockerized))
        if dockerized:
            self.log.critical("----------------------------------------")
            self.log.critical("-[ This session using Selenium/Docker ]-")
            self.log.critical("----------------------------------------")
            self.driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
        else:
            self.log.critical("-----------------------------------------------")
            self.log.critical("-[ This session is NOT using Selenium/Docker ]-")
            self.log.critical("-----------------------------------------------")
            self.driver = webdriver.Chrome(self.CHROME_PATH)

    """
        [Description]
        get_driver
        :return -> self.driver : WebDriver object
    """
    def get_driver(self):
        self.log.info('[BaseTest - Call "get_driver"]')
        return self.driver

    """
        [Description]
        tearDown
        - This method responsible of terminating the browser process.
    """
    def tearDown(self):
        self.log.info('[BaseTest - Call "tearDown"]')
        self.get_driver().close()
        self.get_driver().quit()
