# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -06
# @File: get_request_obj.py
# desc:
from model.dependence_obj import DependenceObj
from model.request_obj import RequestObj


class GetRequestObj:

    @staticmethod
    def get_request_obj(request_dict) -> RequestObj:
        request_info = request_dict.get("request")
        name = request_dict.get("name")
        assertion_list = request_dict.get("assertion")
        uri = request_info['uri']
        method = request_info.get("method")
        headers = request_info.get("headers")
        datas = request_info.get("datas")
        if "dependence" in request_dict.keys():
            dependence = DependenceObj(request_dict.get("dependence"))

        else:
            dependence = None



        request_obj = RequestObj(uri=uri,
                                 method=method,
                                 headers=headers,
                                 name=name,
                                 assertion_list=assertion_list,
                                 datas=datas,
                                 dependence=dependence
                                 )
        return request_obj

