#!/usr/bin/env python
import logging
import time


class Logger(object):

    """
        Static constant of
        the path of logs location
    """
    RUNTIME_LOG_PATH = '/Users/sysmurff/Desktop/GIT/BitlyAut/src/runtime/logs'
    """
        [Description]
        __init__
        - Constructor, construct an object of Logger
    """
    def __init__(self):
        logging.basicConfig(filename='{0}/{1}-runtime.log'.format(self.RUNTIME_LOG_PATH, time.time().__str__()[:10]),
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.DEBUG)
    """
        [Description]
        info 
        - Information logging markup
    """
    @staticmethod
    def info(msg):
        logging.info(msg)

    """ 
        [Description]
        warn
        - Warning logging markup
    """
    @staticmethod
    def warn(msg):
        logging.warning(msg)

    """
        [Description]
        critical
        - Critical logging markup
    """
    @staticmethod
    def critical(msg):
        logging.critical(msg)

    """
        [Description]
        error
        - Error logging markup
    """
    @staticmethod
    def error(msg):
        logging.error(msg)
