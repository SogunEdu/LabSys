# -*- coding:utf-8 -*-
import json

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from common.fields import USERNAME, PASSWD, DATA, META, USER_ID,  EMAIL, MSG, STATUS
from common.base_request_view import BaseRequestView

__author__ = "姜显辉"


class UserLoginView(BaseRequestView):
    def post(self, request):
        """
        用户登录接口

        :param request:
        :return:
        """
        try:
            request_info = json.loads(request.body)
            user = authenticate(username=request_info[USERNAME], password=request_info[PASSWD])

            # 未通过验证
            if user is None:
                self.warning("user[{}] login failed for wrong username or password".format(request_info[USERNAME]))
                response = HttpResponse(json.dumps({
                    DATA: None,
                    META: {
                        MSG: "登录失败",
                        STATUS: 403
                    }
                }))

                response.status_code = 403
                return response

            # 用户没激活
            if not user.is_active:
                self.info("user[{}] login failed for inactive".format(request_info[USERNAME]))
                response = HttpResponse(json.dumps({
                    DATA: None,
                    META: {
                        MSG: "未激活",
                        STATUS: 403
                    }
                }))

                response.status_code = 403
                return response

            # 用户已激活，并且能通过验证
            login(request, user)
            self.info("user[{}] login success".format(request_info[USERNAME]))
            response = HttpResponse(json.dumps({
                DATA: {
                    USERNAME: user.username,
                    USER_ID: user.id,
                    EMAIL: user.email
                },
                META: {
                    MSG: "登录成功",
                    STATUS: 200
                }
            }))

            return response

        except KeyError as err_info:
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

        except Exception as err_info:
            self.error("user login occur exception: {}".format(err_info))

            response = HttpResponse(json.dumps({
                DATA: None,
                META: {
                    MSG: "系统异常",
                    STATUS: 500
                }
            }))
            response.status_code = 500

            return response