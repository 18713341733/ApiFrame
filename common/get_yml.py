# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 04 -24
# @File: get_yml.py
# desc:
# -*- coding:utf-8 -*-
import os
import yaml
from common.get_path import GetPath
from common.my_exception import StatusException,ValueException


class GetYml:

    @staticmethod
    def getValue(file_name,name):
        '''
        实现功能：读取yaml配置文件
        filename: yml文件的路径，如 config/host.yml
        name: yml文件中，具体字段的名称
        '''
        # 找到file_name的目录
        file_path = GetPath.get_other_path(file_name)
        f = open(file_path, 'r', encoding='utf-8')  # 以只读形式打开filename
        x = yaml.safe_load(f)  # 通过load方法转成字典
        f.close()
        try:
            return x[name]
        except Exception as e:
            raise StatusException("{}文件中，不存在{}字段".format(file_name, e))








