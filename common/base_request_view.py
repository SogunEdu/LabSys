# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.views import View
import json
import logging
from common.fields import DATA, META, MSG, STATUS

__author__ = "姜显辉"


class BaseRequestView(View):
    """
    代理logging打印

    """
    def debug(self, msg, *args, **kwargs):
        logging.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        logging.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        logging.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        logging.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        logging.critical(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        logging.log(level, msg, *args, **kwargs)


class LogRequiredView(BaseRequestView):
    """
    当需要登录时，使用这个基类

    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            response = HttpResponse(json.dumps({
                DATA: None,
                META: {
                    MSG: "未登录",
                    STATUS: 401
                }
            }))
            response.status_code = 401

            return response

        return super().dispatch(request, *args, **kwargs)



