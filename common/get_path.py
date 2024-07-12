# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 04 -24
# @File: get_path.py
# desc: 获取各种路径

import os
import sys


class GetPath:

    @staticmethod
    def get_project_path():
        """获取项目的跟路径"""
        # 获取文件目录
        curPath = os.path.abspath(os.path.dirname(__file__))
        # 获取项目根路径，内容为当前项目的名字
        rootPath = curPath[:curPath.find('ApiFrame') + len('ApiFrame')]
        return rootPath

    @staticmethod
    def get_other_path(abspath: str):
        """从根目录下开始获取其他路径"""
        # 调用了上述获得项目根目录的方法
        rootPath = GetPath.get_project_path()
        dataPath = os.path.abspath(rootPath + str(abspath))
        return dataPath

    @staticmethod
    def resource_path(relative_path):
        """获得路径，当前文件所在路径"""
        # 是否Bundle Resource
        if getattr(sys, 'frozen', False):
            # running in a bundle
            base_path = sys._MEIPASS
            print('true', base_path)
        else:
            # running live
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    x = GetPath.resource_path("get_path.py")
    print(x)
