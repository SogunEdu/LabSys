# -*- coding:utf-8 -*-

from django.db import models
from teaching_info.models.class_info import ClassInfo
from teaching_info.models.course import Course
from users.models.user import User

__author__ = "姜显辉"


class Schedule(models.Model):
    class_id = models.ForeignKey(ClassInfo, on_delete=models.CASCADE, db_column='class_id')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "course_schedule"
        app_label = "course_schedule"
