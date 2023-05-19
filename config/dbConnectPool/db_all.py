# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -12
# @File: db_all.py
# desc:
from common.db_utils import DbUtils
from common.get_yml import GetYml
from common.singleton import singleton

@singleton
def get_baidu_manage_db_conn():
    db_obj = GetYml.get_yml_dbobj("/config/db.yml","test_db")
    conn = DbUtils.get_db_conn(db_obj)
    return conn