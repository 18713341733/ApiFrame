# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2022 - 06 -10
# @File: singleton.py
#coding:utf-8
#单例模式函数，用来修饰类
def singleton(cls,*args,**kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args,**kw)
        return instances[cls]
    return _singleton
