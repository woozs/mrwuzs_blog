# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 19:14
# @Author  : mrwuzs
# @Email   : mrwuzs@163.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views


urlpatterns = [
    path('update_comment', views.update_comment, name='update_comment')
]
