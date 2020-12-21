#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 18:32
# @Author  : Qun He
# @File    : tasks_entry.py
# @Software: PyCharm

import importlib

from conf_holder import ConfHolder
from db_holder import DBHolder
from path_holder import PathHolder
from tasks_executor import TasksExecutor
from utils.logging_utils import Logger


"""
|  TasksExecutor (Singleton)
|--Method: prepare_chain, finish_chain, release_close_chain
|   > xxx_task --> TaskWorker (Singleton)
|   > ..........._task --> TaskWorker (Singleton)
|   > ..........._task --> TaskWorker (Singleton)
|--Method: do_execute (multi process copy instances in different memory automatically)
|   > yyy_task --> TaskWorker (Prototype)
|   > ..........._task --> TaskWorker (Prototype)
|   > ..........._task --> TaskWorker (Prototype)
"""

if __name__ == "__main__":

    # init the 2 holders
    conf_holder = ConfHolder()
    db_holder = DBHolder()

    # load base config
    base_conf = conf_holder.singleton_base_conf()

    mongo_conf = base_conf.get('mongo')
    redis_conf = base_conf.get('redis')
    task_conf = base_conf.get('task')

    # prepare mongo info
    mongo_ip = mongo_conf.getattr('ip')
    mongo_port = mongo_conf.getattr('port')
    mongo_db = mongo_conf.getattr('database')
    mongo_coll = mongo_conf.getattr('collection_test')

    # prepare redis info
    redis_ip = redis_conf.getattr('ip')
    redis_port = redis_conf.getattr('port')
    redis_db = redis_conf.getattr('db')

    # task list
    task_list = task_conf.getattr('task_list').split('\n')

    # prepare all of the worker instances from each package
    # NOTICE: these instances only can be used in current process.
    task_workers = [
        importlib.import_module(task_package).TaskWorker(
            task_name=task_package,
            base_conf=base_conf,
            # init the logger only for current process, the logger will be reset in multiprocess pool.
            logger=Logger('INFO', name=task_package, log_name=task_package,
                          log_path=PathHolder.LOG_PATH)
        ) for task_package in task_list
    ]

    # init the tasks executor
    tasks_executor = TasksExecutor(
        task_workers,
        logger=Logger('INFO', name='tasks_executor', log_path=PathHolder.LOG_PATH, log_name='task_executor'),
        base_conf=base_conf,
        redis_conn=db_holder.singleton_redis_connector(ip=redis_ip, port=redis_port, db_name=redis_db),
        mongo_conn=db_holder.singleton_mongo_connector(ip=mongo_ip, port=mongo_port, db_name=mongo_db, coll_name=mongo_coll)
    )
    # do the jobs
    tasks_executor.prepare_chain()
    # NOTICE:in execute_chain method the multiprocess will be used.
    tasks_executor.execute_chain()
    tasks_executor.finish_chain()
    tasks_executor.release_close_chain()
