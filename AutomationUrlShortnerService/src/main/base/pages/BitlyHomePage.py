#!/usr/bin/env python
from AutomationUrlShortnerService.src.main.base.BasePage import BasePage


class BitlyHomePage(BasePage, object):

    def __init__(self, driver):
        super(BitlyHomePage, self).__init__(driver)
        self._title = self.get_page_title()
        self._url = self.get_page_url()
        self.init_elements()

    def init_elements(self):
        try:
            self.URL_INPUT_FIELD = self._driver.find_element_by_xpath("//*[@id='shorten_url']")
            self.COOKIE_LAYOUT_DIALOG_X_BTN = self._driver.find_element_by_xpath("//*[@class='close-icon']")
            self.PROMO_DIALOG_X_BTN = self._driver.find_element_by_xpath("//*[@id='promo-close']")
            self.SHORTEN_BTN = self._driver.find_element_by_xpath("//*[@id='shorten_btn']")
        except Exception as err:
            print('{0}'.format(err))

    def shorten_link(self, link):
        try:
            self.close_cookie_dialog()
            self.wait()
            self.clear_send_keys(self.URL_INPUT_FIELD, link)
            self.click(self.SHORTEN_BTN)
            self.close_promotion_dialog()
            return self.get_results()
        except Exception as err:
            print('{0}'.format(err))

    def close_cookie_dialog(self):
        try:
            self.wait()
            self.click(self.COOKIE_LAYOUT_DIALOG_X_BTN)
        except Exception as err:
            print('{0}'.format(err))

    def close_promotion_dialog(self):
        try:
            self.wait()
            self.click(self.PROMO_DIALOG_X_BTN)
        except Exception as err:
            print('{0}'.format(err))

    def get_results(self):
        try:
            self.wait()
            res_link = self._driver.find_element_by_css_selector("ul#most_recent_link a.short-url")
            return res_link.text
        except Exception as err:
            print('{0}'.format(err))

    def _get_url(self):
        return self._url

    def _get_title(self):
        return self._title