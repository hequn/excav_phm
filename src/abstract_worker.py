#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 14:43
# @Author  : Qun He
# @File    : abstract_task.py
# @Software: PyCharm

import abc


class AbstractWorker(metaclass=abc.ABCMeta):
    """
    Abstract worker.
    In order to constraint the TaskWorker behavior.
    """
    def __init__(self, task_name='default', base_conf=None, logger=None):
        """
        Init method will be extend by each TaskWorker.
        :param task_name: unique task name.
        :param base_conf: base configuration.
        :param logger: default logger not for multi process.
        """
        self.task_name = task_name
        self.base_conf = base_conf
        self.logger = logger

    @abc.abstractmethod
    def prepare(self):
        raise NotImplementedError("Must provide implementation in subclass.")

    @abc.abstractmethod
    def execute(self, working_data):
        raise NotImplementedError("Must provide implementation in subclass.")

    @abc.abstractmethod
    def finish(self, saved_data, mongo_conn):
        raise NotImplementedError("Must provide implementation in subclass.")

    @abc.abstractmethod
    def release_close(self):
        raise NotImplementedError("Must provide implementation in subclass.")

    @abc.abstractmethod
    def get_unique_name(self):
        raise NotImplementedError("Must provide implementation in subclass.")

    @abc.abstractmethod
    def set_multi_logger(self, logger):
        raise NotImplementedError("Must provide implementation in subclass.")

