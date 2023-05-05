# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 04 -24
# @File: assert_jud.py
# desc: 断言的逻辑判断

import jsonpath,json

class AssertJud:

    @staticmethod
    def assert_jud(assertion_list:list,res:dict) -> bool:
        new_list = []
        for x in assertion_list:

            expectation = x[0]['expectation']
            print("》》》》》》》》》》断言信息：》》》》》》》》》》》》")
            print("expectation期望结果：",expectation)
            compare = x[1]['compare']
            print("compare比较方式:",compare)
            print("compare的类型是,",type(compare))
            ctual_value = x[2]['ctual_value']
            print("ctual_value实际比较的结果（如果为None,则与整个接口返回值做比较）：",ctual_value)

            if ctual_value == None:
                if compare == "=":
                    new_list.append(res == expectation)
                elif "in" == compare:
                    x = expectation in str(res)
                    new_list.append(x)
                    if not x:
                        print("《《《《《《《《《《《断言失败》》》》》》》》》。")
                        print("expectation期望值：", expectation)
                        print("res的值：", res)



                elif compare == ">":
                    new_list.append(res > expectation)
                elif compare == "<":
                    new_list.append(res < expectation)
                else:
                    pass
            else:
                # value 从response中获取用户想要的具体字段
                value = jsonpath.jsonpath(res,ctual_value)[0]
                value = str(value)
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(value)
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if compare == "=":
                    new_list.append(value == expectation)
                elif "in" == compare:
                    x = expectation in str(value)
                    print("expectation,", expectation)
                    print("res的值是,", value)
                    print("x的值是,", x)
                    new_list.append(x)
                elif compare == ">":
                    new_list.append(int(value) > int(expectation))
                elif compare == "<":
                    new_list.append(int(value) < int(expectation))
                else:
                    pass

        if False in new_list:
            return False
        else:
            return True




