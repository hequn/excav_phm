#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 20:12
# @Author  : Qun He
# @File    : redis_utils.py
# @Software: PyCharm

from redis import Redis, BlockingConnectionPool


class RedisConnector:
    """
    A simple wrapper.
    """

    def __init__(self, host='127.0.0.1', port=6379, db=0, password=None, max_pool_size=100, timeout=60):
        self.__conn = Redis(
            connection_pool=BlockingConnectionPool(max_connections=max_pool_size, timeout=timeout,
                                                   host=host, port=port, db=db, password=password))

    def __getattr__(self, command):
        def _(*args):
            """
            Wrapper all the funcs in redis.
            :param args: any.
            :return: the target func
            """
            return getattr(self.__conn, command)(*args)

        return _

    @property
    def connector(self):
        return self.__conn
