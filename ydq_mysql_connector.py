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

    def query(self, sql_query):
        try:
            self.cursor.execute(sql_query)
            return self.cursor
        except mysql.connector.Error as e:
            print 'query error!{}'.format(e)
            return None

if __name__ == '__main__':
    logger.info('test')