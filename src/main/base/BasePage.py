#!/usr/bin/env python
import time
from src.main.base.utils.Wait import Wait


class BasePage(Wait):
    """
        [Description]
        __init__
        :param -> driver : WebDriver Object
        - Constructor, construct an Abstract of BasePage
    """
    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.wait_until_page_loaded()

    """
        [Description]
        click
        :param -> elem : WebElement String locator 
        - clicks on given WebElement Object 
    """
    def click(self, elem):
        self.log.info('Calling "click" on {0}'.format(elem))
        try:
            if elem.is_displayed:
                elem.click()
        except Exception as err:
            self.log.error('Error occurred {0}'.format(err))
            print('{0}'.format(err))

    """
        [Description]
        clear_send_keys
        :param -> elem : WebElement String locator
        :param -> phrase : String Object
        - clear the surface on input filled and send a phrase to it
    """
    def clear_send_keys(self, elem, phrase):
        self.log.info('Calling "clear_send_keys" on {0} -> {1}'.format(elem, phrase))
        try:
            if elem.is_displayed:
                elem.clear()
                self.break_chars_send_keys(elem, phrase)
        except Exception as err:
            self.log.error('Error occurred {0}'.format(err))
            print('{0}'.format(err))

    """
        [Description]
        get_url
        :return -> the url of current website
    """
    def get_page_url(self):
        self.log.info('Calling "get_page_url"')
        return self._driver.current_url

    """
        [Description]
        get_page_title
        :return -> the title of page
    """
    def get_page_title(self):
        self.log.info('Calling "get_page_title"')
        return self._driver.title

    """
        [Description]
        get_page_source
        :return -> the html source of the page
    """
    def get_page_source(self):
        self.log.info('Calling "get_page_source"')
        return self._driver.page_source

    """
        [Description]
        break_chars_send_keys
        :param -> elem : WebElement Object
        :param -> phrase : String Object
        - break a string into chars and send then into the WebElement
    """
    def break_chars_send_keys(self, elem, phrase):
        self.log.info('Calling "break_chars_send_keys"')
        for c in phrase:
            elem.send_keys(c)

    """
        [Description]
        wait
        :param -> sec : Integer 
        - wait an 'x' amount of time 
    """
    def wait(self, sec=1):
        self.log.info('Calling "wait" on {0} seconds'.format(sec))
        time.sleep(sec)

    """
        [Description]
        init_elements
        - Abstract method for webwelements initialization inside POM
    """
    def init_elements(self):
        pass
