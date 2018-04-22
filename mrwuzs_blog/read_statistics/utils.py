# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 17:01
# @Author  : mrwuzs
# @Email   : mrwuzs@163.com
# @File    : utils.py
# @Software: PyCharm
from django.contrib.contenttypes.models import ContentType
from .models import ReadNum

def read_statistics_once_read(requset,obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)
    if not requset.COOKIES.get(key):
        if ReadNum.objects.filter(content_type=ct,object_id=obj.pk).count():
            #存在记录
            readnum = ReadNum.objects.get(content_type=ct,object_id=obj.pk)
        else:
            readnum = ReadNum(content_type=ct,object_id=obj.pk)
        #阅读次数加1
        readnum.read_num +=1
        readnum.save()
    return key








