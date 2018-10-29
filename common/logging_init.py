# -*- coding: utf-8 -*-

from django.conf import settings
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter, StreamHandler

__author__ = '姜显辉'


def init_logging():
    try:
        logger = logging.getLogger()
        logger.setLevel(settings.LOG_LEVEL)

        file_handler = TimedRotatingFileHandler("log/lab_sys.log", when="midnight", backupCount=7)
        logger.addHandler(file_handler)

        formatter = Formatter("%(asctime)s [%(levelname)s]: %(message)s")
        file_handler.setFormatter(formatter)

        if settings.LOG_LEVEL == logging.DEBUG:
            stream_handler = StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

    except Exception as err_info:
        print(err_info)
        exit(-1)
