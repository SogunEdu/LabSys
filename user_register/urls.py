# -*- coding: utf-8 -*-
from django.urls import path

from user_register.views.login import UserLoginView
from user_register.views.logout import UserLogoutView

__author__ = '姜显辉'

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),
]
