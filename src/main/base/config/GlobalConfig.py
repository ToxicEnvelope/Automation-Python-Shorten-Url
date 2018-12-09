#!/usr/bin/env python
import platform
from os.path import expanduser
from src.main.base.utils.Logger import Logger


class GlobalConfig(object):
    """
        Static constant of Logger
        to handle runtime logs for analysis
    """
    logger = Logger()
    """
        [Description]
        __init__(self, args='None')
        :param -> args : str
        - Constructor, construct a GlobalConfig object
    """
    def __init__(self, args='chrome'):
        self.platform_identifier(args)

    """
        [Description]
        platform_identifier(self, commands='None')
        :param -> commands : str 
        - This method responsible to identify 
          which operating system our machine running.
    """
    def platform_identifier(self, commands='chrome'):
        self.logger.info('GlobalConfig - Calling on "platform_identifier" -> {0}'.format(commands))
        p = platform.platform().lower()
        commands = commands.lower()
        if p.startswith('win'):
            self.logger.debug('Setting Configuration for {0}'.format(p))
            self.DRIVER_PATH = self.get_Driver(p, commands)
        elif p.startswith('lin'):
            self.logger.debug('Setting Configuration for {0}'.format(p))
            self.DRIVER_PATH = self.get_Driver(p, commands)
        else:
            self.logger.debug('Setting Configuration for {0}'.format(p))
            self.DRIVER_PATH = self.get_Driver(p, commands)

    """
        [Description]
        get_Driver(self, flag)
        :param -> flag : str
        - This method responsible to 
        set a required Browser available 
        despite the Operating System type
    """
    def get_Driver(self, os, flag):
        self.logger.info('GlobalConfig - Calling on "get_Driver" -> {0} : {1}'.format(os, flag))
        if os.startswith('win') and flag.__eq__('chrome'):
            self.CHROME_PATH = '{0}.exe'.format(self.get_ChromeDriver())
        elif os.startswith('win') and flag.__eq__('phantomjs'):
            self.CHROME_PATH = '{0}.exe'.format(self.get_PhantomDriver())
        elif os.startswith('lin') and flag.__eq__('chrome'):
            self.PHANTOMJS_PATH = '{0}'.format(self.get_ChromeDriver())
        elif os.startswith('lin') and flag.__eq__('phantomjs'):
            self.PHANTOMJS_PATH = '{0}'.format(self.get_PhantomDriver())
        else:
            self.CHROME_PATH = '{0}'.format(self.get_ChromeDriver())

    """
        [Description]
        get_ChromeDriver(self)
        :return -> Executable ChromeDriver path 
    """
    def get_ChromeDriver(self):
        self.logger.info('GlobalConfig - Calling on "get_ChromeDriver"')
        USER_HOME = expanduser("~")
        PROJ_PATH = '{0}\\Desktop\\Git\\Automation-Python-Shorten-Url'.format(USER_HOME)
        BIN_PATH = '{0}\\src\\bin'.format(PROJ_PATH)
        return '{0}\\chromedriver'.format(BIN_PATH)

    """
        [Description]
        get_PhantomDriver(self)
        :return -> Executable PhatomJSDriver path 
    """
    def get_PhantomDriver(self):
        self.logger.info('GlobalConfig - Calling on "get_PhantomDriver"')
        USER_HOME = expanduser("~")
        PROJ_PATH = '{0}\\Desktop\\Git\\Automation-Python-Shorten-Url'.format(USER_HOME)
        BIN_PATH = '{0}\\src\\bin'.format(PROJ_PATH)
        return '{0}\\phantomjs.exe'.format(BIN_PATH)

    """
        [Description]
        get_ScreenshotDir(self)
        :return -> the screenshots directory path 
    """
    def get_ScreenshotDir(self):
        self.logger.info('GlobalConfig - Calling on "get_ScreenshotDir"')
        USER_HOME = expanduser("~")
        PROJ_PATH = '{0}\\Desktop\\Git\\Automation-Python-Shorten-Url'.format(USER_HOME)
        SCREENSHOT_DIR = '{0}\\src\\test\\resources'.format(PROJ_PATH)
        return SCREENSHOT_DIR

    """
        [Description]
        get_LogsDir(self)
        :return -> the logs directory path 
    """
    def get_LogsDir(self):
        self.logger.info('GlobalConfig - Calling on "get_LogsDir"')
        USER_HOME = expanduser("~")
        PROJ_PATH = '{0}\\Desktop\\Git\\Automation-Python-Shorten-Url'.format(USER_HOME)
        LOGS_DIR = '{0}\\runtime\\logs'.format(PROJ_PATH)
        return LOGS_DIR

    """
        [Description]
        get_ResultsDir(self)
        :return -> the results screenshots directory path 
    """
    def get_GhostLogDir(self):
        self.logger.info('GlobalConfig - Calling on "get_GhostLogDir"')
        return '{0}\\ghostlog'.format(self.get_LogsDir())

    """
        [Description]
        get_GridDir(self)
        :return -> the grid screenshots directory path 
    """
    def get_GridDir(self):
        self.logger.info('GlobalConfig - Calling on "get_GridDir"')
        return '{0}\\grid'.format(self.get_ScreenshotDir())

    """
        [Description]
        get_ResultsDir(self)
        :return -> the results screenshots directory path 
    """
    def get_ResultsDir(self):
        self.logger.info('GlobalConfig - Calling on "get_ResultsDir"')
        return '{0}\\results'.format(self.get_ScreenshotDir())
