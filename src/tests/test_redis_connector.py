#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 10:04
# @Author  : Qun He
# @File    : test_redis_connector.py
# @Software: PyCharm

import _init_paths
from unittest import TestCase
from utils.redis_utils import RedisConnector


class TestRedisConnector(TestCase):
    def test_client(self):
        rds = RedisConnector()
        conn = rds.connector
        conn.set('1', '1')
        conn.set('2', '2')
        conn.set('3', '3')
        print(conn.get('1'))
        print(conn.get('2'))
        print(conn.get('3'))
        conn.close()
