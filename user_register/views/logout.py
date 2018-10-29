# -*- coding: utf-8 -*-

import json

from django.contrib.auth import logout
from django.http import HttpResponse

from common.base_request_view import BaseRequestView
from common.fields import DATA, META, MSG, STATUS

__author__ = '姜显辉'


class UserLogoutView(BaseRequestView):
    def post(self, request):
        """
        用户登出接口

        :param request:
        :return:
        """
        try:
            logout(request)
            self.info("user[{}] logout success".format(request.user))
            response = HttpResponse(json.dumps({
                DATA: None,
                META: {
                    MSG: "登录成功",
                    STATUS: 200
                }
            }))

            return response

        except Exception as err_info:
            self.error("user login occur exception: {}".format(err_info))

            response = HttpResponse(json.dumps({
                DATA: None,
                META: {
                    MSG: "缺少字段",
                    STATUS: 400
                }
            }))
            response.status_code = 400

            return response
