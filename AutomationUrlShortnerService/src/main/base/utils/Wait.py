#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Wait:

    def __init__(self, driver=webdriver.Chrome()):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 15, 300)

    def wait_visibility(self, elem_ref):
        elem = self.make_webelement(elem_ref)
        self._wait.until(EC.visibility_of_element_located, elem)

    def wait_for_presence(self, elem_ref):
        elem = self.make_webelement(elem_ref)
        self._wait.until(EC.presence_of_element_located, elem)

    def make_webelement(self, elem_tpl):
        elem = self._driver.find_element(elem_tpl)
        return elem

    def wait_until_page_loaded(self):
        self._wait.until(EC.visibility_of_element_located, (By.XPATH, "html"))

    def wait_click(self, elem):
        """
        Todo - Implementation of smart wait_click
        :param elem:
        :return:
        """
        pass

    def wait_send_keys(self, elem, phrase):
        """
        Todo - Implementation of smart wait_send_keys
        :param elem:
        :param phrase:
        :return:
        """
        pass
