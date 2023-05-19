# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -12
# @File: db_obj.py
# desc:
class DbObj:
    def __init__(self,name,host,port,user_name,password):
        self.name=name
        self.host=host
        self.port=port
        self.user_name=user_name
        self.password=password

    def __str__(self):
        info = "\n 数据库的name:{}\n host:{}\n port:{}\n user_name:{}\n password:{}\n ".format(
            self.name,
            self.host,
            self.port,
            self.user_name,
            self.password
        )
        return info
