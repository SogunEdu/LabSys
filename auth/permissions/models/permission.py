# -*- coding:utf-8 -*-

from django.db import models

__author__ = "姜显辉"


class Permission(models.Model):
    """
    权限表
    """
    id = models.AutoField(primary_key=True)
    auth_name = models.CharField(max_length=20)
    level = models.SmallIntegerField()
    # 父类权限id
    pid = models.ForeignKey('self', on_delete=models.CASCADE, db_column='pid')
    path = models.FilePathField()

    class Meta:
        app_label = "permissions"
        db_table = "permission"

