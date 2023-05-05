# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 04 -27
# @File: handle_str_utils.py
# desc: 处理、替换字字符串
import re
from common.global_dict import get_value,set_value


class HandleStrUtils:

    # 完整的请求是一个dic datas
    # 替换的关键词也是一个字典 dependence_expectation_obj
    @staticmethod
    def replace_dict_to_dict(datas:dict,dependence_expectation_obj:dict) -> dict:
        datas.update(dependence_expectation_obj)
        return datas


    # 判断url字符串是否以http开头，如果不是的话，自动补全url
    @staticmethod
    def check_url(url:str,host:str) -> str:
        if url.startswith("http"):
            return url
        else:
            return host+url

    # 处理请求datas中的变量，id: ${id}
    @staticmethod
    def replace_var(datas:dict) -> dict:
        for key, value in datas.items():
            var_list = re.findall(r"\$\{(.*?)\}", str(value))
            if len(var_list) > 0:
                for i in var_list:
                    expectation_value = get_value(i)
                    print(expectation_value)
                    # 替换字符串
                    pattern = r"\$\{" + i + r"\}"
                    print("pattern：", pattern)
                    print("value:", value)
                    value = re.sub(pattern, str(expectation_value), value)
                    print("result", value)

                    # 判断获取的数据类型
                    # 如果为int类型
                    if isinstance(expectation_value, int) and str(expectation_value) == str(value):
                        datas[key] = int(value)
                    else:
                        datas[key] = value
        print("datas>>>>>>>>>>>>>>",datas)
        return datas


