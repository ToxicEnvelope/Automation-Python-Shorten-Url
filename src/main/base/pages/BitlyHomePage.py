#!/usr/bin/env python
from src.main.base.BasePage import BasePage


class BitlyHomePage(BasePage, object):
    """
        [Description]
        __init__
        :param -> driver : WebDriver Object
        - Constructor, construct an Abstract of BasePage
    """
    def __init__(self, driver):
        super(BitlyHomePage, self).__init__(driver)
        self._title = self.get_page_title()
        self._url = self.get_page_url()
        self.init_elements()

    """
        [Description]
        init_elements
        - Initialize the page WebElement Objects
          that we want to work with in at the very start 
    """
    def init_elements(self):
        self.log.info('BitlyHomePage - Calling "init_elements"')
        try:
            self.URL_INPUT_FIELD = self._driver.find_element_by_xpath("//*[@id='shorten_url']")
            self.COOKIE_LAYOUT_DIALOG_X_BTN = self._driver.find_element_by_xpath("//*[@class='close-icon']")
            self.PROMO_DIALOG_X_BTN = self._driver.find_element_by_xpath("//*[@id='promo-close']")
            self.SHORTEN_BTN = self._driver.find_element_by_xpath("//*[@id='shorten_btn']")
        except Exception as err:
            self.log.error('BitlyHomePage - Error occurred {0}'.format(err))
            print('{0}'.format(err))

    """
        [Description]
        shorten_link
        :param -> link : String object
        :return -> self.get_results() function
        - Functional E2E operation that insert
          a given link to an input field, submit it
          and return the results of the new shorten link
    """
    def shorten_link(self, link):
        self.log.info('BitlyHomePage - Calling "shorten_link" on {0}'.format(link))
        try:
            self.close_cookie_dialog()
            self.wait()
            self.clear_send_keys(self.URL_INPUT_FIELD, link)
            self.click(self.SHORTEN_BTN)
            self.close_promotion_dialog()
            return self.get_results()
        except Exception as err:
            self.log.error('BitlyHomePage - Error occurred {0}'.format(err))
            print('{0}'.format(err))

    """
        [Description]
        close_cookie_dialog
        - Simulate a click on some WebElement 
          so it will close it
    """
    def close_cookie_dialog(self):
        self.log.info('BitlyHomePage - Calling "close_cookie_dialog"')
        try:
            self.wait()
            self.click(self.COOKIE_LAYOUT_DIALOG_X_BTN)
        except Exception as err:
            self.log.error('BitlyHomePage - Error occurred {0}'.format(err))
            print('{0}'.format(err))

    """
        [Description]
        close_promotion_dialog
        - Simulate a click on some WebElement 
          so it will close it
    """
    def close_promotion_dialog(self):
        self.log.info('BitlyHomePage - Calling "close_promotion_dialog"')
        try:
            self.wait()
            self.click(self.PROMO_DIALOG_X_BTN)
        except Exception as err:
            self.log.error('BitlyHomePage - Error occurred {0}'.format(err))
            print('{0}'.format(err))

    """
        [Description]
        get_results
        :return -> res_link.text : String
        - This method find the result of a shorten link
          and return it's text value
    """
    def get_results(self):
        self.log.info('BitlyHomePage - Calling "get_results"')
        try:
            self.wait()
            res_link = self._driver.find_element_by_css_selector("ul#most_recent_link a.short-url")
            return res_link.text
        except Exception as err:
            self.log.error('BitlyHomePage - Error occurred {0}'.format(err))
            print('{0}'.format(err))

    """
        [Description]
        _get_url
        :return -> the url of the page
    """
    def _get_url(self):
        self.log.info('BitlyHomePage - Calling "_get_url"')
        return self._url

    """
        [Description]
        _get_title
        :return -> the tile of the page
    """
    def _get_title(self):
        self.log.info('BitlyHomePage - Calling "_get_title"')
        return self._title
