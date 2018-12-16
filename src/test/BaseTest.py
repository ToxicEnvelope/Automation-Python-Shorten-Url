#!/usr/bin/env python
import time
from selenium import webdriver
from src.main.base.utils.Logger import Logger
from src.main.base.config.GlobalConfig import GlobalConfig
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BaseTest(object):
    """
       Static constant of GlobalConfig
       for configuration management
   """
    config = GlobalConfig('chrome')
    """
        Docker flag variable
    """
    docker_flag = False
    #docker_flag = True
    """
        [Description]
        setUp
        :param -> dockerized : Boolean
        - This method responsible of starting up the browser process.
          If `dockerized=True` then docker session will take place,
          Otherwise local session will take place.
    """
    def setUp(self, dockerized=docker_flag):
        self.config.logger.info('{0} - Calling on "setUp" -> is_docker {1}'.format(__name__, dockerized))
        if dockerized:
            self.config.logger.critical("#########################################")
            self.config.logger.critical("# This session is USING Selenium/Docker #")
            self.config.logger.critical("#########################################")
            self.driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
        else:
            self.config.logger.critical("#############################################")
            self.config.logger.critical("# This session is NOT using Selenium/Docker #")
            self.config.logger.critical("#############################################")
            self.driver = webdriver.Chrome(self.config.CHROME_PATH)

    """
        [Description]
        get_driver
        :return -> self.driver : WebDriver object
    """
    def get_driver(self):
        self.config.logger.info('{0} - Calling on "get_driver"'.format(__name__))
        return self.driver

    """
        [Description]
        tearDown
        - This method responsible of terminating the browser process.
    """
    def tearDown(self):
        self.config.logger.info('{0} - Calling on "tearDown"'.format(__name__))
        self.get_driver().close()
        self.get_driver().quit()

    """
        [Description]
        get_timstamp(self)
        :return -> timestamp : str
    """
    def get_timestamp(self):
        self.config.logger.info('{0} - Calling on "get_timestamp"'.format(__name__))
        return int(time.time().__str__()[:10])
