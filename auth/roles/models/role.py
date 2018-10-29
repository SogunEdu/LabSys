# -*- coding:utf-8 -*-

from django.db import models
from auth.permissions.models.permission import Permission
from django.conf import settings

__author__ = "姜显辉"


class Role(models.Model):
    """
    角色表
    """
    # 角色名
    name = models.CharField(verbose_name="", max_length=20, unique=True)
    # 角色职能描述
    desc = models.TextField()
    # 权限
    permission = models.ManyToManyField(
        Permission,
        through='RolePermission'
    )

    class Meta:
        app_label = "roles"
        db_table = "role"


class RolePermission(models.Model):
    """
    授权表

    """
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    auth_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "roles"
        db_table = "role_permission"
