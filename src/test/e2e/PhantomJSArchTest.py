import unittest
from src.test.BaseTest import BaseTest
from src.main.base.pages.BitlyHomePage import BitlyHomePage


class MyTestCase(BaseTest, unittest.TestCase):

    link = 'https://github.com/ToxicEnvelope/Automation-Python-Shorten-Url'
    bitly_url = 'https://bitly.com'

    def test_something(self):
        driver = self.get_driver()
        driver.get(self.bitly_url)
        bitPage = BitlyHomePage(driver)
        short_link = bitPage.shorten_link(self.link)
        bitPage.get_PhantomDriver().screenshot(self.link, 'STAGING.png')
        bitPage.get_PhantomDriver().capture_screens()
        bitPage.get_PhantomDriver().screenshot(short_link, 'PRODUCTION.png')
        bitPage.get_PhantomDriver().capture_screens()
        bitPage.get_PhantomDriver().analyze()


if __name__ == '__main__':
    unittest.main()
