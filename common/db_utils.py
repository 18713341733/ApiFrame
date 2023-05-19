# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -12
# @File: db_utils.py
# desc:
from model.db_obj import DbObj
import pymysql

class DbUtils:

    @staticmethod
    def get_db_conn(db_obj:DbObj)->pymysql.connections.Connection:
        conn = pymysql.connect(
            host=db_obj.host,
            user=db_obj.user_name,
            password=db_obj.password,
            port=db_obj.port,
            charset="utf8"  # 编码
        )
        return conn

    @staticmethod
    def execute_sql(conn:pymysql.connections.Connection,sql:str)->str:
        result = ""
        # 获取一个游标
        cursor = conn.cursor()
        # 去除字符串中前后的空白
        sql = sql.strip()
        # 判断sql语句的增删改查
        if sql.startswith("SELECT") or sql.startswith("select"):
            try:
                cursor.execute(sql)  # 执行sql语句
                result = cursor.fetchall()  # 所有结果
                print(result)
            except Exception as e:
                conn.rollback()
                raise Exception("查询失败",e)
            finally:
                cursor.close()  # 关闭当前游标
        else:
            try:
                cursor.execute(sql)  # 执行sql语句，也可执行数据库命令，如：show tables
                conn.commit()  # 增删改，必须执行事务
                print("数据更新成功")
            except Exception as e:
                conn.rollback()  # 若出现失败，进行回滚
                raise Exception("数据更新失败",e)
            finally:
                cursor.close()  # 关闭当前游

        return result



