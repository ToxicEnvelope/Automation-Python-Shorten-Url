#!/usr/bin/env python
import time
from selenium import webdriver
from src.main.base.utils.Grid import Grid


class VR(Grid, object):
    """
        [Description]
        __init__(self, driver)
        :param -> driver : WebDriver Object
        - Constructor, construct a VR (VirtualRegression) Object
    """
    def __init__(self, driver):
        super(VR, self).__init__()
        self._driver = driver
        self._phantom = webdriver.PhantomJS(
            service_log_path='{0}\\{1}-ghostdriver.log'.format(self.config.get_GhostLogDir(),
                                                               time.time().__str__()[:10]))

    """
        [Description]
        capture_screens(self, namespace_test=None):
        :param -> namespace_test : str (=None)
    """
    def capture_screens(self, namespace_test=None):
        self.config.logger.debug('{0} - Calling on "capture_screens" -> {1}'.format(__name__, namespace_test))
        if namespace_test is not None:
            self.screenshot(self._driver.current_url, '{0}-{1}.png'.format(time.time().__str__()[:10], namespace_test))
            self.screenshot(self._phantom.current_url, '{0}-{1}.png'.format(time.time().__str__()[:10], namespace_test))
        else:
            self.screenshot(self._driver.current_url, '{0}-{1}.png'.format(time.time().__str__()[:10], 'Staging'))
            self.screenshot(self._phantom.current_url, '{0}-{1}.png'.format(time.time().__str__()[:10], 'Production'))

    """
        [Description]
        screenshot(self, url, file_name=None)
        :param -> url : str
        :param -> file_name : str (=None)
    """
    def screenshot(self, url, file_name):
        self.config.logger.debug('{0} - Calling on "screenshot" -> {1}, {2}'.format(__name__, url, file_name))
        self._phantom.get(url)
        time.sleep(2)
        self._phantom.set_window_size(1024, 768)
        self._phantom.save_screenshot('{0}\\{1}'.format(self.config.get_ScreenshotDir(), file_name))
        time.sleep(2)
        out_file = self._phantom.get_screenshot_as_png()
        time.sleep(2)
        self._phantom.save_screenshot('{0}\\{1}'.format(self.config.get_ScreenshotDir(), out_file))
        time.sleep(2)
        print("Done.")
        return self.open_image('{0}\\{1}'.format(self.config.get_ScreenshotDir(), file_name))

    """
        [Description]
        analyze(self, staging_file, production_file)
        :param -> staging_file
        :param -> production_file
    """
    def analyze(self, staging_file="STAGING.png", production_file='PRODUCTION.png'):
        self.config.logger.debug('{0} - Calling on "analyze" -> stgfile: {1}, prdfile: {2}'.format(__name__,
                                                                                                   staging_file,
                                                                                                   production_file))
        screenshot_staging = self.open_image('{0}\\{1}'.format(self.config.get_ScreenshotDir(), staging_file))
        screenshot_production = self.open_image('{0}\\{1}'.format(self.config.get_ScreenshotDir(), production_file))
        columns = 60
        rows = 80
        screen_width, screen_height = screenshot_staging.size
        block_width = ((screen_width - 1) // columns) + 1 # this is just a division ceiling
        block_height = ((screen_height - 1) // rows) + 1

        for y in range(0, screen_height, block_height+1):
            for x in range(0, screen_width, block_width+1):
                region_staging = self.process_region(screenshot_staging, x, y, block_width, block_height)
                region_production = self.process_region(screenshot_production, x, y, block_width, block_height)

                if region_staging is not None and region_production is not None and region_production != region_staging:
                    draw = self.draw_image(screenshot_staging)
                    draw.rectangle((x, y, x+block_width, y+block_height), outline="red")

        screenshot_staging.save('{0}\\{1}-result.png'.format(self.config.get_ResultsDir(), time.time().__str__()[:10]))

    """
        [Description]
        process_region(self, image, x, y, width, height)
        :param -> image
        :param -> x
        :param -> y
        :param -> width
        :param -> height
        :return -> adiviation of region_total / factor
    """
    def process_region(self, image, x, y, width, height):
        self.config.logger.debug('{0} - Calling on "process_region" -> {1}, {2}, {3}, {4}, {5}'.format(__name__,
                                                                                                        image,
                                                                                                        x,
                                                                                                        y,
                                                                                                        width,
                                                                                                        height))
        region_total = 0

        # This can be used as the sensitivity factor, the larger it is the less sensitive the comparison
        factor = 100

        for coordinateY in range(y, y+height):
            for coordinateX in range(x, x+width):
                try:
                    pixel = image.getpixel((coordinateX, coordinateY))
                    region_total += sum(pixel)/4
                except:
                    return

        return region_total/factor
