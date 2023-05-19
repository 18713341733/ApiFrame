# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 04 -26
# @File: my_exception.py
# desc: 测试项目自定义的异常

# 接口状态异常
class StatusException(Exception):
    def __init__(self, errorinfo):
        super().__init__(self)
        self.errorinfo = errorinfo

    def __str__(self):
        return self.errorinfo

# 返回值异常
class ValueException(Exception):
    def __init__(self, errorinfo):
        super().__init__(self)
        self.errorinfo = errorinfo

    def __str__(self):
        return self.errorinfo
