# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 20:58
# @Author  : mrwuzs
# @Email   : mrwuzs@163.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views


urlpatterns = [
    path('',views.blog_list,name='blog_list'),
    path('<int:blog_pk>',views.blog_detail,name = 'blog_detail'),
    path('type/<int:type_pk>',views.blogs_with_type,name = 'blogs_with_type'),
    path('date/<int:year>/<int:month>',views.blogs_with_date,name = 'blogs_with_date'),


]



