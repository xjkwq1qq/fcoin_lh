# -*- coding:utf-8 -*-
# fcoin的api调用工具类
import fcoin
import traceback
import time
from fcoin.cons import *
import json

# api类
api_key = '6ee8c12a0b004c1c839f7d38645c1873'
api_secret = '711a4cc685ee4a02a3958072edb1a1f7'
api = fcoin.authorize(api_key, api_secret)

# 配置信息
# python使用ft币总量的比例，全部是100
python_use = 5
# 设置ft不备卖出的比例，全部是100
lock_ft = 15
symbol = 'ftusdt'


class fcoin_api_utils(object):
    def candles(self, resolution, symbol):
        while True:
            try:
                return api.public_request(GET, api.http_market + 'candles/%s/%s' % (resolution, symbol))
            except Exception:
                traceback.print_exc()

    # 分析波动趋势
    def fluctuation_trend(self):
        result = self.candles('M1', symbol)
        print result['data']
        # 极大和极小，以及当前所在区间
        # enumerate 同时获取索引和数据
        max_info = None
        min_info = None
        for index, item in enumerate(result['data']):
            if max_info:
                if max_info.bf:
                    pass


        print len(result)

    def parse_js(self, expr):
        """
        解析非标准JSON的Javascript字符串，等同于json.loads(JSON str)
        :param expr:非标准JSON的Javascript字符串
        :return:Python字典
        """
        obj = eval(expr, type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())
        return obj


api_utils = fcoin_api_utils()

if __name__ == '__main__':
    ####################### 行情接口##########################
    # 查询服务器时间
    # print(api.server_time())
    # 查询可用交易对
    # print(api.symbols())

    # 获取成交明细-当前交易数据
    print(api.get_trades(symbol))

    # 获取最新的深度明细--买卖量
    # print(api.get_depth('L20', symbol))

    # 获取成交明细
    # print(api.get_ticker(symbol))

    # 获取成交历史 通过这个进行判定
    # print(candles('M1', symbol))


    ################## 账号接口#############################
    # 查询账户资产
    # print(api.get_balance())

    ###################订单相关##############
    # payload = {'symbol': symbol}
    # print(api.list_orders(payload=json.dumps(payload)))

    # api_utils.fluctuation_trend()
