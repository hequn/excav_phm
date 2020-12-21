#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 14:16
# @Author  : Qun He
# @File    : battery_voltage_low_task.py
# @Software: PyCharm

import _init_paths
from abstract_worker import AbstractWorker


class TaskWorker(AbstractWorker):
    """
    The TaskWorker concentrate on business date processing.
    The class name can't be changed in any task.
    """

    def prepare(self):
        """
        Prepare some params or files using in the task and save them into self as instance members.
        NOTICE: the method should only be executed once.
        :return: None
        """
        # TODO: do something.
        self.logger.info('Write the log in prepare for ' + self.task_name)
        return

    def execute(self, working_data):
        """
        Execute process logical codes for each excavator data.
        NOTICE: the method will be executed in each process for processing batch data.
        :param working_data:{
                               'SY100': [{'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 414},
                                         {'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 424},
                                         ...
                                         {'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 434}],
                               'SY101': [{'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 414},
                                         {'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 424},
                                         ...
                                         {'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 434}],
                               ......,
                               'SY102': [{'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 414},
                                         {'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 424},
                                         ...
                                         {'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 434}],
                               'SY103': [{'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 414},
                                         {'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 424},
                                         ...
                                         {'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 434}]
                            }
        :return: result_data
                { # we should know who is the task owner
                   'battery_voltage_low_task.battery_voltage_low_worker':
                   [
                       ['SY100', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
                       ['SY101', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
                       ......
                       ['SY102', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
                       ['SY103', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0]
                   ]
                 }
        """
        self.logger.info('Write the log in execute for ' + self.task_name)
        self.logger.info(working_data)
        result_data = {}
        # reconstruct_data:
        # [
        #   ['SY100', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
        #   ['SY101', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
        #   ......,
        #   ['SY102', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
        #   ['SY103', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0]
        # ]
        reconstruct_data = []
        # get the key and value in working data,
        # key is machine id ,value is today's working data array.
        for key in working_data:
            ############################################################################################################
            # TODO:add you logical codes.
            #  key:working_data.get(key)
            #  e.g.:'SY100': [
            #                     {'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 414},
            #                     {'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 424},
            #                     ......
            #                     {'AA': 'AA1', 'BB': 'BB1', 'CC': 16895467844, 'DD': 0.23, 'EE': 434}
            #                ]
            ############################################################################################################
            # TODO:trick the data for temporary used to illustrate the result data structure.
            reconstruct_data.append([key, '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0])
        result_data.update({self.task_name: reconstruct_data})
        return result_data

    def finish(self, saved_data, mongo_conn):
        """
        Write self.result_data to file system or mongodb.
        NOTICE: the method should only be executed once.
        :return: None
        :param saved_data: the entire task result for this worker, you can batch store them.
        [
            ['SY100', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
            ['SY110', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
            ......
            ['SY130', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
            ['SY101', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0],
            ['SY111', '2', 3, 4.0, '1', '2', 3, 4.0, '1', '2', '河北', '承德', '1', '2', 3, 4.0]
        ]
        :param mongo_conn: the mongodb singleton instance.
        :return: None
        """
        self.logger.info('Write the log in finish for ' + self.task_name)
        self.logger.info(saved_data)
        # trick the mongo collection header
        header = ['serialNo', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'prov', 'city', 'l', 'm', 'n', 'p']
        for record in saved_data:
            # TODO: do something.
            # we can also use pipeline to save batch records to db
            # op_1 = Operation('coll', 'insert_one', {'hello': 'heaven'})
            # op_2 = Operation('coll', 'insert_one', {'hello': 'hell'})
            # op_3 = Operation('coll', 'insert_one', {'hello': 'god'})
            # op_4 = Operation('coll', 'find', kwargs={'limit': 2}, callback=cursor_callback)
            # op_5 = Operation('coll', 'find_one', {'hello': 'god'})
            # pipeline = [op_1, op_2, op_3, op_4, op_5]
            # rst = mongo_conn.transaction_pipeline(pipeline)
            mongo_conn.coll.insert_one(dict(zip(header, record)))
        return

    def release_close(self):
        """
        Release something or close something.
        :return: None
        """
        # TODO: do something.
        self.logger.info('Write the log in release_close for ' + self.task_name)
        return

    def get_unique_name(self):
        """
        Get the unique task name.
        :return: task name (must be unique)
        """
        return self.task_name

    def set_multi_logger(self, logger):
        """
        Set the multi logger.
        :param logger: multi logger.
        :return: None
        """
        self.logger = logger
