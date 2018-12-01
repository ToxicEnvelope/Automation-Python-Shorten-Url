#!/usr/bin/env python
from selenium.webdriver.common.by import By
from src.main.base.utils.Logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Wait:
    """
        Static constant of Logger
        to handle runtime logs for analysis
    """
    log = Logger()
    """
        [Description]
        __init__
        :param -> driver : WebDriver Object
        - Constructor, construct an Abstract of Wait
    """
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 15, 300)

    """
        [Description]
        wait_visibility
        :param -> elem_ref : Page locator (By , String)
        - For future caching implementation
          waiting for visibility for webelement
    """
    def wait_visibility(self, elem_ref):
        elem = self.make_webelement(elem_ref)
        self._wait.until(EC.visibility_of_element_located, elem)

    """
        [Description]
        wait_for_presence
        :param -> elem_ref : Page locator (By , String)
        - For future caching implementation
          waiting for presence for webelement
    """
    def wait_for_presence(self, elem_ref):
        elem = self.make_webelement(elem_ref)
        self._wait.until(EC.presence_of_element_located, elem)

    """
        [Description]
        make_webelement
        :param -> elem_tpl : Tuple Object
        - Construct a WebElement by given (how, using) core Locator of Selenium
    """
    def make_webelement(self, elem_tpl):
        by, loc = elem_tpl
        elem = self._driver.find_element((by, loc))
        return elem

    """
        [Description]
        wait_until_page_loaded
        - Wait until the main page HTML fully
          visible after render
    """
    def wait_until_page_loaded(self):
        self._wait.until(EC.visibility_of_element_located, (By.XPATH, "html"))

    """
        [Description]
        wait_click
        - For future implementation
          use smart waiting more efficiently
    """
    def wait_click(self, elem):
        """
        Todo - Implementation of smart wait_click
        :param elem:
        :return:
        """
        pass

    """
        [Description]
        wait_send_keys
        - For future implementation
          use smart waiting more efficiently
    """
    def wait_send_keys(self, elem, phrase):
        """
        Todo - Implementation of smart wait_send_keys
        :param elem:
        :param phrase:
        :return:
        """
        pass
