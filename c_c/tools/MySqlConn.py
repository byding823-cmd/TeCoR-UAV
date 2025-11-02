# -*- coding: utf-8 -*-
"""
@Author  : DY
@Software: PyCharm
@Date    : 2025/1/3 18:30
"""

import pymysql

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'ur_orders40',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}
connection = pymysql.connect(**config)
def database_op(sql, datas=None):
    try:
        with connection.cursor() as cursor:
            if sql[0]=='I' or sql[0]=='i':
                if datas is not None:
                    cursor.execute(sql,datas)
                else:
                    cursor.execute(sql)
                connection.commit()
                return True
            elif sql[0]=='S' or sql[0]=='s':
                cursor.execute(sql)
                res = cursor.fetchall()
                connection.commit()
                return res
            elif sql[0]=='D' or sql[0]=='d':
                cursor.execute(sql)
                connection.commit()
                return True
            elif sql[0]=='U' or sql[0]=='u':
                cursor.execute(sql)
                connection.commit()
                return True
    except Exception as e:
        connection.rollback()
        print(f"ERR: {e}")


def getdata():
    orders = database_op('select * from `orders`')
    ve = database_op('select * from `ve`')
    graph = database_op('select * from `graph`')
    goods = database_op('select * from `goods`')
    stores = database_op('select * from `stores`')
    box = database_op('select * from `box`')
    return orders, ve, graph, goods, stores,box