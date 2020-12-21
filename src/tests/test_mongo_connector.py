#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 20:20
# @Author  : Qun He
# @File    : test_mongo_connector.py
# @Software: PyCharm

import _init_paths
from unittest import TestCase
from utils.mongo_utils import MongoConnector


class TestDBManager(TestCase):
    def test_client(self):
        dbm = MongoConnector('mongodb://localhost:27017/admin')  # db_name, coll_name default 'test'
        print(dbm.coll.find_one())  # {'_id': ObjectId('...'), 'hello': 'world'}
