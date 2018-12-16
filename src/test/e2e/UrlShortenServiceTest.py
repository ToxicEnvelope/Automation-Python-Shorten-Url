#!/usr/bin/env python
import unittest
from src.test.BaseTest import BaseTest
from src.main.base.pages.BitlyHomePage import BitlyHomePage


class UrlShortenService(BaseTest, unittest.TestCase):

    link = 'https://github.com/ToxicEnvelope/Automation-Python-Shorten-Url'
    bitly_url = 'https://bitly.com'

    def test_attempt_to_shorten_utl(self):
        self.config.logger.info('{0} - Calling "test_attempt_to_shorten_utl"')
        driver = self.get_driver()
        driver.get(self.bitly_url)
        bitly_home_page = BitlyHomePage(self.driver)

        self.config.logger.info('{0} - [Current Site URL "{1}"]'.format(__name__, bitly_home_page._get_url()))
        self.config.logger.info('{0} - [Current Website Title "{1}"]'.format(__name__, bitly_home_page._get_title()))

        self.config.logger.info('{0} - [Feeding Service With "{1}"]'.format(__name__, self.link))
        short_link = bitly_home_page.shorten_link(self.link)

        self.config.logger.info('{0} - [Navigate to "{1}"]'.format(__name__, short_link))
        driver.get(short_link)
        self.config.logger.info('{0} - [Current Site URL "{1}"]'.format(__name__, driver.current_url))
        self.config.logger.info('{0} - [Current Website Title "{1}"]'.format(__name__, driver.title))

        self.config.logger.info('{0} - Asserting Titles')
        # Assert on Titles
        assert not driver.title.__eq__(bitly_home_page._get_title()), \
            'Assertion Failed: Expecting "{0}"' .format(driver.title)
        self.config.logger.info('UrlShortenService - Asserting URLs')
        # Assert on URLs
        assert not driver.current_url.__eq__(bitly_home_page._get_url()), \
            'Assertion Failed: Expecting "{0}"'.format(driver.current_url)


if __name__ == "__main__":
    unittest.main()
