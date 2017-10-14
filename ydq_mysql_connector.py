# -*- coding: UTF-8 -*-

import logging
import mysql.connector

logger = logging.getLogger(__file__)

config = {
    'host': 'localhost',
    'user': 'root',
    'port': 3306,
    'database': 'test',
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

    def exect_query(self, sql_query):
        try:
            self.cursor.execute(sql_query)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print 'query error!{}'.format(e)
            return None

    def exect_no_query(self, sql_query):
        try:
            self.cursor.execute(sql_query)
            self.cnn.commit()
        except mysql.connector.Error as e:
            print 'query error!{}'.format(e)

if __name__ == '__main__':
    ydq_mysql = YdqMysql()
    ydq_mysql.exect_no_query(r"insert into table1 values('2', 'lisi')")
    ydq_mysql.exect_no_query(r"insert into table2 values('2', '1')")

    for row in ydq_mysql.exect_query(r"select * from table2"):
        print row[0], row[1]