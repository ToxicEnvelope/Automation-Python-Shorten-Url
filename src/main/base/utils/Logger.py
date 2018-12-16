#!/usr/bin/env python
import time
import logging
import coloredlogs


class Logger(object):
    """
        Static constant of
        the path of logs location
    """
    RUNTIME_LOG_PATH = '/Users/yahav.hoffman/Desktop/Git/Automation-Python-Shorten-Url/src/runtime/logs'
    """
        [Description]
        __init__
        - Constructor, construct an object of Logger
    """
    def __init__(self):
        logging.basicConfig(filename='{0}/{1}-runtime.log'.format(self.RUNTIME_LOG_PATH, time.time().__str__()[:10]),
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        coloredlogs.install(level='DEBUG', logger=self.logger)

    """
        [Description]
        debug 
        - Debugging logging markup
    """
    def debug(self, msg):
        self.logger.debug(msg)

    """
        [Description]
        info 
        - Information logging markup
    """
    def info(self, msg):
        self.logger.info(msg)

    """ 
        [Description]
        warn
        - Warning logging markup
    """
    def warn(self, msg):
        self.logger.warning(msg)

    """
        [Description]
        critical
        - Critical logging markup
    """
    def critical(self, msg):
        self.logger.critical(msg)

    """
        [Description]
        error
        - Error logging markup
    """
    def error(self, msg):
        self.logger.error(msg)
