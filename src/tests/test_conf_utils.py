#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 16:36
# @Author  : Qun He
# @File    : test_conf_utils.py
# @Software: PyCharm

import _init_paths
from unittest import TestCase
from utils.conf_utils import Config


class TestConfig(TestCase):
    def test_get(self):
        conf = Config('baseConfig')
        print(conf.get("mongo").getattr('ip'))
        print(conf.mongo.getattr('ip'))
        print(conf.get("mongo").getattr('client'))
        print(conf.mongo.getattr('client'))
        print(conf.get("mongo").getattr('collection_fs'))
        print(conf.mongo.getattr('collection_fs'))
