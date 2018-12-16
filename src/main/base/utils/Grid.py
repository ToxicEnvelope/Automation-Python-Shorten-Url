#!/usr/bin/env python
from PIL import Image, ImageDraw
from src.main.base.config.GlobalConfig import GlobalConfig


class Grid(object):
    """
        Static implementation of
        GlobalConfig for configuration
    """
    config = GlobalConfig()
    """
        [Description]
        __init__(self)
        - Constructor, construct a Grid object
    """
    def __init__(self):
        pass

    """
        [Description]
        open_image(self, abs_img_path)
        :param -> abs_img_path : str
        :return -> Image object
        - This method responsible to 
        open an image file given absolute path
        
    """
    def open_image(self, abs_img_path):
        self.config.logger.debug('{0} - Calling on "open_image" -> {1}'.format(__name__, abs_img_path))
        return Image.open(abs_img_path)

    """
        [Description]
        draw_image(self, screenshot)
        :param -> screnshot : Image object
        :return -> Drawable object
        - This method responsible to
        create a drawable source from given Image object
    """
    def draw_image(self, screenshot):
        self.config.logger.debug('{0} - Calling on "draw_image" -> {1}'.format(__name__, screenshot))
        return ImageDraw.Draw(screenshot)

    """
        [Description]
        capture_image(self)
        - Main capture logic
    """
    def capture_image(self):
        self.config.logger.debug('{0} - Calling on "capture_image"'.format(__name__))
        screenshot = self.open_image('{0}\\screen_staging.png'.format(self.config.get_ScreenshotDir()))
        columns = 60
        rows = 80
        screen_width, screen_height = screenshot.size

        block_width = ((screen_width - 1) // columns) + 1 # this is just a division ceiling
        block_height = ((screen_height - 1) // rows) + 1

        for y in range(0, screen_height, block_height):
            for x in range(0, screen_width, block_width):
                draw = self.draw_image(screenshot)
                draw.rectangle((x, y, x+block_width, y+block_height), outline='red')

        screenshot.save('{0}\\grid\\grid.png'.format(self.config.get_ScreenshotDir()))


if __name__ == '__main__':
    g = Grid()
