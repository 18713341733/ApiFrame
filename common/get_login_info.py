# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 04 -25
# @File: get_login_info.py
# desc: 获取登录后的相关信息。
import requests
import json
from common.my_exception import StatusException,ValueException

from common.get_yml import GetYml


class GetLoginInfo:

    # 获取登录的url（测试项目平台）
    baidu_manager_pc_host = GetYml.getValue("/config/host.yml", "baidu_manager_pc_test")
    login_uri = GetYml.getValue("/config/uri.yml", "baidu_manager_pc_login_uri")
    login_url = baidu_manager_pc_host + login_uri



    # （测试项目平台）
    @staticmethod
    def get_login_info(username=None, password=None):
        url = GetLoginInfo.login_url
        datas = {
            "codexxx": "11xxx"
        }
        if username == None and password == None:
            # 获取登录的账号密码
            user_obj = GetYml.getValue("/config/user.yml", "baidu-manager-pc-user")
            username = user_obj["username"]
            password = user_obj["password"]
        else:
            pass

        datas["username"] = username
        datas["password"] = password
        headers = {
            "Content-Type":"application/json",
            "Accept-Encoding":"gzip, deflate, br"
        }
        datas = json.dumps(datas)
        try:
            res = requests.request(method="post", url=url, data=datas, headers=headers).json()
        except:
            raise StatusException("统一获取用户的登录信息时，登录报错")

        return res

    # （测试项目平台）
    @staticmethod
    def get_token(username=None, password=None):
        if username == None and password == None:
            res = GetLoginInfo.get_login_info()
        else:
            res = GetLoginInfo.get_login_info(username, password)

        token = res["data"]["token"]
        return token

    # （测试项目平台）
    @staticmethod
    def get_authorization(username=None, password=None):
        if username == None and password == None:
            res = GetLoginInfo.get_login_info()
        else:
            res = GetLoginInfo.get_login_info(username, password)
        token = res["data"]["token"]
        authorization = "Bearer " + token
        return authorization

    # （测试项目平台）
    @staticmethod
    def get_authorization_and_token(username=None, password=None):
        if username == None and password == None:
            res = GetLoginInfo.get_login_info()
        else:
            res = GetLoginInfo.get_login_info(username, password)
        token = res["data"]["token"]
        authorization = "Bearer " + token
        return authorization,token

