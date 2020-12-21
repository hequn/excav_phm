#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 11:44
# @Author  : Qun He
# @File    : test_logging_utils.py
# @Software: PyCharm

import _init_paths
from unittest import TestCase
from utils.logging_utils import Logger


class TestLogger(TestCase):
    def test_logger(self):
        x = Logger('INFO', name='tasks_executor', log_path='D:/logs', log_name=str(1))
        x.logger.info(111)
        x.logger.debug(111)
        x.logger.error(111)
        x.logger.warning(111)
        x.info(222)
        x.debug(222)
        x.error(222)
        x.warning(222)
        return
