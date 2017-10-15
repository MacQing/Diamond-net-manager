# -*- coding: UTF-8 -*-

import logging
import mysql.connector

logger = logging.getLogger(__file__)

config = {
    'host': 'localhost',
    'user': 'root',
    'port': 3306,
    'database': 'diamond_net_manager',
    'charset': 'utf8'
}

class YdqMysql:
    cnn = None
    cursor = None

    def __init__(self):
        try:
            self.cnn = mysql.connector.connect(**config)
        except mysql.connector.Error as e:
            print 'connect fails!{}'.format(e)

        self.cursor = self.cnn.cursor()

    def __del__(self):
        self.cursor.close()
        self.cnn.close()

    def exect_query(self, sql, params):
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()
        except Exception, e:
            print 'query error! {}'.format(e)
            return None

    def exect_no_query(self, sql, params):
        try:
            self.cursor.execute(sql, params)
            self.cnn.commit()
            return True
        except Exception, e:
            print 'query error! {}'.format(e)
            return False

    def exect_multi_no_query(self, sql_query_list):
        try:
            for sql, params in sql_query_list:
                self.cursor.execute(sql, params)
            self.cnn.commit()
            return True
        except Exception, e:
            print 'query error! {}'.format(e)
            return False

if __name__ == '__main__':
    ydq_mysql = YdqMysql()

    # 检查是否库存充足
    check_sql_query = r"select storage_num from {} where material='{}' and spec='{}' and color='{}' and hight='{}';".format('storage_num', 'sd',  '12', 'd', '32')
    check_res = ydq_mysql.exect_query(check_sql_query)

    if check_res:
        print check_res[0]
    else:
        print check_res
