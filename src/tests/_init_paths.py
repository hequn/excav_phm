#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 19:07
# @Author  : Qun He
# @File    : init_paths.py
# @Software: PyCharm

import os.path as osp
import sys


def add_path(path):
    """
    Add custom path into PYTHONPATH.
    :param path: the custom path.
    :return: None
    """
    if path not in sys.path:
        sys.path.insert(0, path)


this_dir = osp.dirname(__file__)

# Add lib to PYTHONPATH
lib_path = osp.join(this_dir, '..', '..', 'src')
add_path(lib_path)
