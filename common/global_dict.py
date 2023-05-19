# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -04
# @File: global_dict.py
# desc: 全局字典
import jsonpath

from common.singleton import singleton


@singleton
class GlobalDict:
    global_dict = {}



def set_value(key, value):
        # 定义一个全局变量
        GlobalDict().global_dict[key] = value


def get_value(key):
    # 获得一个全局变量，不存在则提示读取对应变量失败
    try:
        return GlobalDict().global_dict[key]
    except Exception as e:
        raise Exception("获取的字典key不存在",e)

# 判断是否存在某个key
def has_key(key):
    if key in GlobalDict().global_dict.keys():
        return True
    else:
        return False









