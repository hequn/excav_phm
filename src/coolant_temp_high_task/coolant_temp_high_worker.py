#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 14:16
# @Author  : Qun He
# @File    : coolant_high_worker.py
# @Software: PyCharm

import _init_paths
from abstract_worker import AbstractWorker


class TaskWorker(AbstractWorker):

    def prepare(self):
        """
        Prepare some params or files.
        :return:
        """
        self.logger.info('Write the log in prepare for ' + self.task_name)
        return

    def execute(self, working_data):
        """
        The method will be executed for each excavator.
        :param working_data:
        :return:
        """
        self.logger.info('Write the log in execute for ' + self.task_name)
        self.logger.debug(working_data)
        result_data = {}
        reconstruct_data = []
        for key in working_data:
            reconstruct_data.append([key, '3', 4, 5.0, '6', '7', 3, 9.0, '8', '2', 8, 4.0, '1', '2', 3, 4.0])
        result_data.update({self.task_name: reconstruct_data})
        return result_data

    def finish(self, saved_data, mongo_conn):
        """
        Write self.result_data to file system and mongodb
        :return:
        """
        self.logger.info('Write the log in finish for ' + self.task_name)
        return

    def release_close(self):
        """
        Release something or close something.
        :return:
        """
        self.logger.info('Write the log in release_close for ' + self.task_name)
        return

    def get_unique_name(self):
        return self.task_name

    def set_multi_logger(self, logger):
        self.logger = logger
