# -*- coding:utf-8 -*-

from django.db import models

__author__ = "姜显辉"


class Course(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()

    class Meta:
        app_label = "teaching_info"
        db_table = "course"
