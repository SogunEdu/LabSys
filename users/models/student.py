# -*- coding:utf-8 -*-

from django.db import models
from users.models.user import User
from teaching_info.models.class_info import ClassInfo

__author__ = "姜显辉"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    class_id = models.ForeignKey(ClassInfo, on_delete=models.CASCADE, db_column='class_id')

    class Meta:
        app_label = 'users'
        db_table = 'student'
