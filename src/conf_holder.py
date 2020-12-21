#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 20:12
# @Author  : Qun He
# @File    : conf_loader.py
# @Software: PyCharm

from utils.conf_utils import Config


class ConfHolder:
    """
    Hold all of the configuration in the project.
    """
    def __init__(self):
        self.base_conf = None
        pass

    def singleton_base_conf(self):
        if self.base_conf is None:
            self.base_conf = Config('baseConfig')
        return self.base_conf
