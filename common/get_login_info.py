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

    # 获取百度登录的url
    baidu_pc_host = GetYml.getValue("/config/host.yml", "baidu_test")
    login_uri = GetYml.getValue("/config/uri.yml", "baidu_login_uri")
    login_url = baidu_pc_host + login_uri

    # 获取搜狗另一个平台的登录的url
    sougou_pc_host = GetYml.getValue("/config/host.yml", "sousou_host")
    login_uri_bms = GetYml.getValue("/config/uri.yml", "sougou_uri")
    login_url_bms = sougou_pc_host + login_uri_bms


    @staticmethod
    def get_login_info(username=None, password=None):
        url = GetLoginInfo.login_url
        datas = {
            "code": "11"
        }
        if username == None and password == None:
            # 获取登录的账号密码
            user_obj = GetYml.getValue("/config/user.yml", "sougou-pc-user")
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


    @staticmethod
    def get_token(username=None, password=None):
        if username == None and password == None:
            res = GetLoginInfo.get_login_info()
        else:
            res = GetLoginInfo.get_login_info(username, password)

        token = res["data"]["token"]
        return token


    @staticmethod
    def get_authorization(username=None, password=None):
        if username == None and password == None:
            res = GetLoginInfo.get_login_info()
        else:
            res = GetLoginInfo.get_login_info(username, password)
        authorization = res["data"]["token"]
        return authorization


    @staticmethod
    def get_login_info_bms(username=None, password=None):
        url = GetLoginInfo.login_url_bms
        datas = {
        }
        if username == None and password == None:
            # 获取登录的账号密码
            user_obj = GetYml.getValue("/config/user.yml", "baidu-pc-user")
            username = user_obj["username"]
            password = user_obj["password"]
        else:
            pass

        datas["loginName"] = username
        datas["password"] = password
        headers = {
            "Content-Type":"application/json",
            "Accept-Encoding":"gzip, deflate, br"
        }
        datas = json.dumps(datas)

        res = requests.request(method="post", url=url, data=datas, headers=headers).json()
        return res

    @staticmethod
    def get_token_bms(username=None, password=None):
        if username == None and password == None:
            try:
                res = GetLoginInfo.get_login_info_bms()
            except:
                raise StatusException("统一获取用户的登录信息时，登录报错")
        else:
            try:
                res = GetLoginInfo.get_login_info_bms(username, password)
            except:
                raise StatusException("统一获取用户的登录信息时，登录报错")

        try:
            token = res["data"]["token"]
        except:
            raise StatusException("统一获取用户的登录信息时，账号密码错误")

        return token


if __name__ == '__main__':

    authorization = GetLoginInfo.get_token_bms("miaojiang","1234561")
    print(authorization)

