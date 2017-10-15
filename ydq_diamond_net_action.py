# -*- coding: UTF-8 -*-

from ydq_mysql_connector import YdqMysql


def in_storage(record_user, material, spec, color, hight, in_storage_num, in_storage_date):
    """
    入库
    :param record_user:
    :param material:
    :param color:
    :param hight:
    :param in_storage_date:
    :param in_storage_num:
    :return:
    """
    ydq_mysql = YdqMysql()

    operation = '入库'

    in_storage_log_sql_query = "insert into in_out_storage_log (operation, operation_user, material, spec, color, hight, operation_num, operation_date) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    in_storage_log_sql_params = (operation, record_user, material, spec, color, hight, in_storage_num, in_storage_date)
    storage_num_sql = "insert into storage_num (material, spec, color, hight, storage_num, update_date) values (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE storage_num = storage_num + %s, update_date = %s"
    storage_num_params = (material, spec, color, hight, in_storage_num, in_storage_date, in_storage_num, in_storage_date)

    try:
        # 执行sql
        status = ydq_mysql.exect_multi_no_query([(in_storage_log_sql_query, in_storage_log_sql_params), (storage_num_sql, storage_num_params)])
        return status
    except Exception, e:
        print e.message
        return False


def out_storage(record_user, material, spec, color, hight, out_storage_num, out_storage_date):
    """
    出库
    :param record_user:
    :param material:
    :param color:
    :param hight:
    :param out_storage_date:
    :param out_storage_num:
    :return:
    """
    ydq_mysql = YdqMysql()

    operation = '出库'

    # 检查是否库存充足
    check_sql_query = "select storage_num from storage_num where material=%s and spec=%s and color=%s and hight=%s"
    check_sql_params = (material, spec, color, hight)
    check_res = ydq_mysql.exect_query(check_sql_query, check_sql_params)
    if check_res is None:
        print '数据库连接错误！'
        return False
    if not check_res or check_res[0][0] < out_storage_num:
        print '库存不足！'
        return False

    out_storage_log_sql_query = "insert into in_out_storage_log (operation, operation_user, material, spec, color, hight, operation_num, operation_date) values (%s, %s,%s,%s,%s,%s,%s,%s)"
    out_storage_log_sql_pamrams = (operation, record_user, material, spec, color, hight, out_storage_num, out_storage_date)
    storage_num_sql_query = "insert into storage_num (material, spec, color, hight, storage_num, update_date) values (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE storage_num = storage_num - %s, update_date = %s"
    storage_num_sql_params = (material, spec, color, hight, out_storage_num, out_storage_date, out_storage_num, out_storage_date)

    try:
        # 执行sql
        status = ydq_mysql.exect_multi_no_query([(out_storage_log_sql_query, out_storage_log_sql_pamrams), (storage_num_sql_query, storage_num_sql_params)])
        return status
    except Exception, e:
        print e.message
        return False


def show_in_out_storage_log(material, spec, color, hight, begin_date, end_date, is_in=True):
    ydq_mysql = YdqMysql()

    operation = '入库' if is_in else '出库'

    try:
        sql_query = "select material, spec, color, hight, operation_date, operation_num, operation_user from in_out_storage_log where material=%s and spec=%s and color=%s and hight=%s and operation=%s and (operation_date between %s and %s) "
        sql_params = (material, spec, color, hight, operation, begin_date, end_date)
        sql_res = ydq_mysql.exect_query(sql_query, sql_params)

        res = []
        for row in sql_res:
            res.append(dict(material=row[0], spec=row[1], color=row[2], hight=row[3], operation_date=row[4].__str__(), operation_num=row[5], operation_user=row[6]))
        return res
    except Exception, e:
        print e.message
        return None


def show_storage_num_all():
    ydq_mysql = YdqMysql()

    try:
        sql_query = "select material, spec, color, hight, storage_num, update_date from storage_num"
        sql_res = ydq_mysql.exect_query(sql_query, None)

        res = []
        for row in sql_res:
            res.append(dict(material=row[0], spec=row[1], color=row[2], hight=row[3], storage_num=row[4], update_date=row[5].__str__()))
        return res
    except Exception, e:
        print e.message
        return None