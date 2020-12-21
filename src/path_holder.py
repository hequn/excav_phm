#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 20:12
# @Author  : Qun He
# @File    : syspath_utils.py
# @Software: PyCharm

import os


class PathHolder:
    """
    Hold all of the paths the project needs.
    """
    # project root path
    PROJ_PATH = os.path.dirname(
        # package src
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    CONF_PATH = os.path.join(PROJ_PATH, 'conf')

    LOG_PATH = os.path.join(PROJ_PATH, 'logs')

    def __init__(self):
        pass
