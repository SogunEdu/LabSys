# -*- coding: utf-8 -*-

from django.db import models
from labs.models.lab_task import LabTask
from users.models.student import Student

__author__ = '姜显辉'


class LabResult(models.Model):
    task = models.ForeignKey(LabTask, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    commit_data = models.FilePathField()
    commit_date = models.DateTimeField()
    score = models.FloatField()

    class Meta:
        app_label = "labs"
        db_table = "lab_result"
