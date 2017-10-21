# -*- coding: UTF-8 -*-

import tornado.web
import json
import logging

from ydq_diamond_net_action import *

logger = logging.getLogger(__file__)

# 入库
class DiamondNetInStorageHandler(tornado.web.RequestHandler):
    def post(self):
        res = dict()
        try:
            param = self.request.body.decode('utf-8')
            param = json.loads(param)

            record_user = param['record_user']
            material = param['material']
            spec = param['spec']
            color = param['color']
            hight = param['hight']
            operation_num = param['operation_num']
            operation_date = param['operation_date']

            status, msg = in_storage(record_user, material, spec, color, hight, operation_num, operation_date)

            res['status'] = status
            res['msg'] = msg
            logger.info(msg)
        except Exception, e:
            res['status'] = False
            res['msg'] = e.message
            logger.info('fail')
        finally:
            self.write(json.dumps(res).encode('utf-8'))



# 出库
class DiamondNetOutStorageHandler(tornado.web.RequestHandler):
    def post(self):
        res = dict()
        try:
            param = self.request.body.decode('utf-8')
            param = json.loads(param)

            record_user = param['record_user']
            material = param['material']
            spec = param['spec']
            color = param['color']
            hight = param['hight']
            operation_num = param['operation_num']
            operation_date = param['operation_date']

            status, msg = out_storage(record_user, material, spec, color, hight, operation_num, operation_date)

            res['status'] = status
            res['msg'] = msg
        except Exception, e:
            res['status'] = False
            res['msg'] = e.message
        finally:
            self.write(json.dumps(res).encode('utf-8'))


# 查看入库出库情况
class DiamondNetShowInOutStorageLogHandler(tornado.web.RequestHandler):
    def post(self):
        res = dict()
        try:
            param = self.request.body.decode('utf-8')
            param = json.loads(param)

            is_in = True if param['is_in'] == '1' else False
            material = param['material']
            spec = param['spec']
            color = param['color']
            hight = param['hight']
            begin_date = param['begin_date']
            end_date = param['end_date']

            status, sql_res, msg = show_in_out_storage_log(material, spec, color, hight, begin_date, end_date, is_in=is_in)

            res['status'] = status
            res['result'] = sql_res
            res['msg'] = msg
            # if sql_res is None:
            #     res['status'] = False
            # else:
            #     res['status'] = True
            #     res['result'] = sql_res
        except Exception, e:
            res['status'] = False
            res['msg'] = e.message
        finally:
            self.write(json.dumps(res).encode('utf-8'))


# 查看库存情况
class DiamondNetShowStorageNumHandler(tornado.web.RequestHandler):
    def get(self):
        res = dict()
        try:
            status, sql_res, msg = show_storage_num_all()

            res['status'] = status
            res['result'] = sql_res
            res['msg'] = msg
            # if sql_res is None:
            #     res['status'] = False
            # else:
            #     res['status'] = True
            #     res['result'] = sql_res
        except Exception, e:
            res['status'] = False
            res['msg'] = e.message
        finally:
            self.write(json.dumps(res).encode('utf-8'))