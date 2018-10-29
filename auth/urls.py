# -*- coding: utf-8 -*-
from django.urls import path, include
from auth.views.menus import MenuView


__author__ = '姜显辉'

urlpatterns = [
    path('menus/', MenuView.as_view()),
    path('permissions/', include('auth.permissions.urls')),
    path('roles/', include('auth.roles.urls')),
]
