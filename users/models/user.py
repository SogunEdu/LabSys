# -*- coding:utf-8 -*-

from django.db import models
from auth.roles.models.role import Role
import re
from django.conf import settings

__author__ = "姜显辉"


def validate_mobile_num(phone_num):
    phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[367]|18\d|19\d)\d{8}$')
    return re.match(phone_pat, phone_num) is not None


class User(models.Model):
    """
    用户包含了角色信息
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, auto_created=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    # 用户电话号码
    phone = models.CharField(max_length=11, validators=[validate_mobile_num], unique=True)
    photo = models.FilePathField(unique=True)
    birth_day = models.DateField()

    class Meta:
        app_label = "users"
        db_table = "user"
