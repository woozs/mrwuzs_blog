# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 14:00
# @Author  : mrwuzs
# @Email   : mrwuzs@163.com
# @File    : views.py
# @Software: PyCharm
from django.shortcuts import render_to_response


def home(request):
    context = {}
    return render_to_response('home.html',context)
