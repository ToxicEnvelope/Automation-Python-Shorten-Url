import unittest
import time
from src.test.BaseTest import BaseTest
from src.main.base.pages.BitlyHomePage import BitlyHomePage


class PhantomJSArch(BaseTest, unittest.TestCase):

    link = 'https://github.com/ToxicEnvelope/Automation-Python-Shorten-Url'
    bitly_url = 'https://bitly.com'

    stag_pic = '{0}{1}STAGING.png'.format(time.time().__str__()[:10], __name__)
    prod_pic = '{0}{1}PRODUCTION.png'.format(time.time().__str__()[:10], __name__)

    def test_something(self):
        self.config.logger.info('{0} - Calling on "test_something"'.format(__name__))
        start_time = self.get_timestamp()

        driver = self.get_driver()
        driver.get(self.bitly_url)
        bitPage = BitlyHomePage(driver)
        short_link = bitPage.shorten_link(self.link)
        stag_file = bitPage.get_PhantomDriver().screenshot(self.link, self.stag_pic)
        prod_file = bitPage.get_PhantomDriver().screenshot(short_link, self.prod_pic)
        bitPage.get_PhantomDriver().analyze(self.stag_pic, self.prod_pic)
        end_time = self.get_timestamp()

        self.config.logger.debug('Test took {0} seconds...'.format(end_time-start_time))
        self.assertEqual(stag_file._repr_png_(), prod_file._repr_png_(),
                         'Asert Failed [{0} is not {1}]'.format(stag_file, prod_file))


if __name__ == '__main__':
    unittest.main()
