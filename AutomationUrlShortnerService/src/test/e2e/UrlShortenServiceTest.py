#!/usr/bin/env python
import unittest
from AutomationUrlShortnerService.src.test.BaseTest import BaseTest
from AutomationUrlShortnerService.src.main.base.pages.BitlyHomePage import BitlyHomePage


class UrlShortenService(BaseTest, unittest.TestCase):

    link = 'https://github.com/ToxicEnvelope/Automation-Python-Shorten-Url'
    bitly_url = 'https://bitly.com'

    def test_attempt_to_shorten_utl(self):
        driver = self.get_driver()
        driver.get(self.bitly_url)
        bitly_home_page = BitlyHomePage(self.driver)

        print('[Current Site URL "{0}"]'.format(bitly_home_page._get_url()))
        print('[Current Website Title "{0}"]'.format(bitly_home_page._get_title()))

        print('[Feeding Service With "{0}"]'.format(self.link))
        short_link = bitly_home_page.shorten_link(self.link)

        print('[Navigate to "{0}"]'.format(short_link))
        driver.get(short_link)
        print('[Current Site URL "{0}"]'.format(driver.current_url))
        print('[Current Website Title "{0}"]'.format(driver.title))

        # Assert on Titles
        assert not driver.title.__eq__(bitly_home_page._get_title()), \
            'Assertion Failed: Expecting "{0}"' .format(driver.title)
        # Assert on URLs
        assert not driver.current_url.__eq__(bitly_home_page._get_url()), \
            'Assertion Failed: Expecting "{0}"'.format(driver.current_url)


if __name__ == "__main__":
    unittest.main()
