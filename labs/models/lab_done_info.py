# -*- coding: utf-8 -*-

from django.db import models

from labs.models.lab_task import LabTask
from users.models.student import Student
from users.models.user import User

__author__ = '姜显辉'


class LabDoneInfo(models.Model):
    """
    作业完成情况

    """
    task = models.ForeignKey(LabTask, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    commit_data = models.FilePathField(null=True)
    commit_date = models.DateTimeField(null=True)
    score = models.FloatField(null=True)
    remark_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = "labs"
        db_table = "lab_result"
