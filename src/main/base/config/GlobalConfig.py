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
        __init__
        - Constructor, construct a GlobalConfig object
    """
    def __init__(self):
        self.platform_identifier()

    """
        [Description]
        platform_identifier
        - This method responsible to identify 
          which operating system our machine running.
    """
    def platform_identifier(self):
        self.logger.info('GlobalConfig - Calling on "platform_identifier"')
        p = platform.platform()
        if p.lower().startswith('win'):
            self.logger.debug('Setting Configuration for {0}'.format(p))
            USER_HOME = expanduser("~")
            PROJ_PATH = '{0}\\Desktop\\Git\\Automation-Python-Shorten-Url'.format(USER_HOME)
            BIN_PATH = '{0}\\src\\bin'.format(PROJ_PATH)
            self.CHROME_PATH = '{0}\\chromedriver.exe'.format(BIN_PATH)
        elif p.lower().startswith('lin'):
            self.logger.debug('Setting Configuration for {0}'.format(p))
            USER_HOME = expanduser("~")
            PROJ_PATH = '{0}\\Desktop\\Git\\Automation-Python-Shorten-Url'.format(USER_HOME)
            BIN_PATH = '{0}\\src\\bin'.format(PROJ_PATH)
            self.CHROME_PATH = '{0}\\chromedriver'.format(BIN_PATH)
        else:
            self.logger.debug('Setting Configuration for {0}'.format(p))
            USER_HOME = expanduser("~")
            PROJ_PATH = '{0}\\Desktop\\Git\\Automation-Python-Shorten-Url'.format(USER_HOME)
            BIN_PATH = '{0}\\src\\bin'.format(PROJ_PATH)
            self.CHROME_PATH = '{0}\\chromedriver'.format(BIN_PATH)
