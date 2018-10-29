# -*- coding: utf-8 -*-

from common.base_request_view import LogRequiredView
from django.http import JsonResponse
from common.fields import DATA, META, MSG, STATUS, PERMISSION_ID, AUTH_NAME, ACCESS_PATH, SUB_MENU
from auth.roles.models.role import Role

__author__ = '姜显辉'


class MenuView(LogRequiredView):
    def get(self, request):
        try:
            role_id = request.user.user.role_id

            # 获取角色所有权限
            role_info = Role.objects.get(id=role_id)
            # 从顶层组装菜单
            menus = self.pack_menu_info(role_info, None)

            if menus is None:
                response = JsonResponse({
                    DATA: None,
                    META: {
                        MSG: "系统异常",
                        STATUS: 500
                    }
                })

                response.status_code = 500
                return response

            return JsonResponse({
                DATA: menus,
                META: {
                    MSG: "获取菜单成功",
                    STATUS: 200
                }
            })

        except Exception as err_info:
            self.error("user[{}] get menus occur exception:{}".format(request.user, err_info))
            response = JsonResponse({
                DATA: None,
                META: {
                    MSG: "系统异常",
                    STATUS: 500
                }
            })

            response.status_code = 500
            return response

    def pack_menu_info(self, role_info, pid):
        try:
            role_permissions = role_info.permission.filter(pid=pid).order_by("id")
            if role_permissions.count() == 0:
                return []

            menu_info = []

            for permission in role_permissions:
                cur_menu = {
                    PERMISSION_ID: permission.id,
                    AUTH_NAME: permission.auth_name,
                    ACCESS_PATH: permission.path,
                    SUB_MENU: []
                }

                sub_menu = self.pack_menu_info(role_info, permission.id)
                # 子菜单获取失败，则全部失败
                if sub_menu is None:
                    return None

                cur_menu[SUB_MENU] = sub_menu

                menu_info.append(cur_menu)

            return menu_info

        except Exception as err_info:
            self.error("user pack menu info occur exception: {}".format(err_info))
            return None


