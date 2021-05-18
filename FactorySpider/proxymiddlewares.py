# -*- coding: utf-8 -*-
import random, base64


class ProxyMiddleware(object):
    # 代理IP列表
    proxyList = [
        '124.88.67.18:80',
        '124.88.67.52:843',
        '110.77.169.30:8080',
        '58.246.194.70:8080',
        '159.232.214.68:8080'
    ]

    def process_request(self, request, spider):
        # 从代理IP列表中随机选择一个
        pro_adr = random.choice(self.proxyList)
        print("USE PROXY -> " + pro_adr)
        request.meta['proxy'] = "http://" + pro_adr
