# -*- coding: utf-8 -*-

from django.db import models
from course_schedule.models.schedule import Schedule
from datetime import datetime

__author__ = '姜显辉'


class LabTask(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True, default="试验")
    data = models.FilePathField(path="/", default=None)
    pub_date = models.DateTimeField(default=datetime.now())
    deadline = models.DateTimeField(default=datetime.now())

    class Meta:
        app_label = "labs"
        db_table = "lab_task"


