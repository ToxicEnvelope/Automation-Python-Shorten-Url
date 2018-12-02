#!/usr/bin/env python
import unittest
from src.test.BaseTest import BaseTest
from src.main.base.pages.BitlyHomePage import BitlyHomePage


class UrlShortenService(BaseTest, unittest.TestCase):

    link = 'https://github.com/ToxicEnvelope/Automation-Python-Shorten-Url'
    bitly_url = 'https://bitly.com'

    def test_attempt_to_shorten_utl(self):
        self.log.info('UrlShortenService - Calling "test_attempt_to_shorten_utl"')
        driver = self.get_driver()
        driver.get(self.bitly_url)
        bitly_home_page = BitlyHomePage(self.driver)

        self.log.info('UrlShortenService - [Current Site URL "{0}"]'.format(bitly_home_page._get_url()))
        self.log.info('UrlShortenService - [Current Website Title "{0}"]'.format(bitly_home_page._get_title()))

        self.log.info('UrlShortenService - [Feeding Service With "{0}"]'.format(self.link))
        short_link = bitly_home_page.shorten_link(self.link)

        self.log.info('UrlShortenService - [Navigate to "{0}"]'.format(short_link))
        driver.get(short_link)
        self.log.info('UrlShortenService - [Current Site URL "{0}"]'.format(driver.current_url))
        self.log.info('UrlShortenService - [Current Website Title "{0}"]'.format(driver.title))

        self.log.info('UrlShortenService - Asserting Titles')
        # Assert on Titles
        assert not driver.title.__eq__(bitly_home_page._get_title()), \
            'Assertion Failed: Expecting "{0}"' .format(driver.title)
        self.log.info('UrlShortenService - Asserting URLs')
        # Assert on URLs
        assert not driver.current_url.__eq__(bitly_home_page._get_url()), \
            'Assertion Failed: Expecting "{0}"'.format(driver.current_url)


if __name__ == "__main__":
    unittest.main()
