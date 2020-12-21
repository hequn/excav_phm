#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 20:12
# @Author  : Qun He
# @File    : task_executor.py
# @Software: PyCharm

import _init_paths
from multiprocessing import Pool
from multiprocessing.managers import BaseManager

from path_holder import PathHolder
from utils.logging_utils import Logger


class TasksExecutor:
    """
    Tasks executor in singleton mode.
    All tasks will be executed as the bellow method order:
        1) prepare_chain
        2) execute_chain
        3) finish_chain
        4) release_close_chain
    """

    def __init__(self, task_workers=None, logger=None, redis_conn=None, mongo_conn=None, base_conf=None):
        self.task_workers = task_workers
        self.logger = logger
        self.redis_conn = redis_conn
        self.mongo_conn = mongo_conn
        self.base_conf = base_conf
        # result dict will store all of the result data:
        # result_dict e.g.
        # {'battery_voltage_low_task.battery_voltage_low_worker': [
        #         ['SY100', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
        #         ['SY110', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
        #         ......，
        #         ['SY130', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
        #         ['SY101', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
        #     ],
        #  ......
        #  'coolant_temp_high_task.coolant_temp_high_worker': [
        #         ['SY100', '3', 4, 5.0, '6', '7', 3, 9.0, '8', '2', 8, 4.0, '1', '2', 3, 4.0],
        #         ['SY110', '3', 4, 5.0, '6', '7', 3, 9.0, '8', '2', 8, 4.0, '1', '2', 3, 4.0],
        #         ......，
        #         ['SY130', '3', 4, 5.0, '6', '7', 3, 9.0, '8', '2', 8, 4.0, '1', '2', 3, 4.0],
        #         ['SY101', '3', 4, 5.0, '6', '7', 3, 9.0, '8', '2', 8, 4.0, '1', '2', 3, 4.0],
        #      ]
        # }
        self.result_dict = {}

    def prepare_chain(self):
        """
        Prepare each task worker.
        :return: None
        """
        for worker in self.task_workers:
            worker.prepare()
        return

    def finish_chain(self):
        """
        Finish all the tasks.
        :return: None
        """
        for worker in self.task_workers:
            # pass the task result data and use mongo_conn to store it
            worker.finish(self.result_dict.get(worker.get_unique_name()), mongo_conn=self.mongo_conn)
        return

    def release_close_chain(self):
        """
        Release and close the task.
        :return: None
        """
        for worker in self.task_workers:
            worker.release_close()
        return

    def execute_chain(self):
        """
        1) Get the redis data (in batch mode accelerating the network transfer).
        2) Define the multi process tasks and the shared logger instance.
        3) Loop to add the async processes to calculate the data result.
        4) Wait all of the jobs return and store the result data in {self.result_dict}.
        :return: result_dict if you want to get it
        """
        # define the pool
        multi_pool = Pool(processes=self.base_conf.get('calculation').getattr('parallelism'))

        # define the multi process shared multi logger
        multi_manager = BaseManager()
        multi_manager.register('Logger', Logger)
        multi_manager.start()
        multi_logger = multi_manager.Logger('INFO', name='multi_task_workers', log_name='multi_task_workers',
                                            log_path=PathHolder.LOG_PATH, multi_logger=False)

        # simulate 100 excavators serialNo
        # TODO: change to the real ids and make them to batch mode
        for i in range(0, 100):
            # TODO: do get the data.
            # get data from redis according to serialNos using pipeline
            # pipe = self.redis_conn.pipeline()
            # pipe.get('1')
            # pipe.get('2')
            # pipe.get('3')
            # pipe_result = pipe.execute()
            # pipe.close()
            # TODO:trick the pipe_result data from redis
            pipe_result = {'SY10' + str(i): [
                {'AA': 'AA1', 'BB': 'BB-' + str(i), 'CC': 16895467844, 'DD': 0.23, 'EE': 414},
                {'AA': 'AA1', 'BB': 'BB-' + str(i), 'CC': 16895467844, 'DD': 0.23, 'EE': 424},
                {'AA': 'AA1', 'BB': 'BB-' + str(i), 'CC': 16895467844, 'DD': 0.23, 'EE': 434}],
                'SY11' + str(i): [
                    {'AA': 'AA1', 'BB': 'BB-' + str(i), 'CC': 16895467844, 'DD': 0.23, 'EE': 414},
                    {'AA': 'AA1', 'BB': 'BB-' + str(i), 'CC': 16895467844, 'DD': 0.23, 'EE': 424},
                    {'AA': 'AA1', 'BB': 'BB-' + str(i), 'CC': 16895467844, 'DD': 0.23, 'EE': 434}],
                'SY12' + str(i): [
                    {'AA': 'AA1', 'BB': 'BB-' + str(i), 'CC': 16895467844, 'DD': 0.23, 'EE': 414},
                    {'AA': 'AA1', 'BB': 'BB-' + str(i), 'CC': 16895467844, 'DD': 0.23, 'EE': 424},
                    {'AA': 'AA1', 'BB': 'BB-' + str(i), 'CC': 16895467844, 'DD': 0.23, 'EE': 434}],
                'SY13' + str(i): [
                    {'AA': 'AA1', 'BB': 'BB-' + str(i), 'CC': 16895467844, 'DD': 0.23, 'EE': 414},
                    {'AA': 'AA1', 'BB': 'BB-' + str(i), 'CC': 16895467844, 'DD': 0.23, 'EE': 424},
                    {'AA': 'AA1', 'BB': 'BB-' + str(i), 'CC': 16895467844, 'DD': 0.23, 'EE': 434}]
            }
            # after each process finished the self.task_result_collector method will be executed.
            # NOTICE: all of the instances will be copied in memory for multi process task.
            #         don't intend to pass any address of your instance to func for using.
            [
                multi_pool.apply_async(
                    func=TasksExecutor.execute_func,
                    args=(worker, pipe_result, multi_logger),
                    callback=self.task_result_collector,
                    error_callback=self.logging_error
                ) for worker in self.task_workers
            ]
        multi_pool.close()
        multi_pool.join()
        multi_manager.shutdown()
        return self.result_dict

    def task_result_collector(self, result_data):
        """
        The callback function which will save the result into self.result_dict.
        :param result_data: callback data.
               { # we should know who is the task owner
                   'xxx_xxx_task.xxx_xxx_worker':
                   [
                       ['SY100', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
                       ['SY101', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
                       ......
                       ['SY102', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
                       ['SY103', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0]
                   ]
               }
        :return: None
        """
        if len(result_data) != 0:
            for key in result_data:
                total_result = self.result_dict.get(key)
                if total_result is None:
                    self.result_dict.update({key: result_data[key]})
                else:
                    total_result.extend(result_data[key])

    def logging_error(self, error_msg):
        """
        Log the error msg.
        :param error_msg: str error msg.
        :return: None
        """
        self.logger.error(error_msg)

    @staticmethod
    def execute_func(worker, working_data, multi_logger):
        """
        Multiprocess target function.
        :param worker: which has been copied in memory for each process, they all have different memory address.
        :param working_data: the excavator's working data (in batch mode).
        :param multi_logger: multi logger is the only shared instance in memory.
        :return: the result data
        """
        worker.set_multi_logger(multi_logger)
        return worker.execute(working_data)
