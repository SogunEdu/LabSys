# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.middleware.csrf import get_token

from common.base_request_view import BaseRequestView

from common.fields import DATA, META, MSG, STATUS, CSRF_TOKEN

__author__ = '姜显辉'


class TokenView(BaseRequestView):
    def get(self, request):
        try:
            token = get_token(request)
            return JsonResponse({
                DATA: {
                    CSRF_TOKEN: token
                },
                META: {
                    MSG: "csrf token获取成功",
                    STATUS: 200
                }
            })

        except Exception as err_info:
            self.error("get token failed: %s", err_info)

            response = JsonResponse({
                DATA: None,
                META: {
                    MSG: "csrf token获取成功",
                    STATUS: 500
                }
            })

            response.status_code = 500
            return response
