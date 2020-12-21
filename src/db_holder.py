#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 12:49
# @Author  : Qun He
# @File    : db_loader.py
# @Software: PyCharm

from utils.mongo_utils import MongoConnector
from utils.redis_utils import RedisConnector


class DBHolder:
    """
    Hold mongo and redis db connectors.
    """

    def __init__(self):
        # the redis connector will be in singleton mode, so keep it
        self.redis_conn = None
        self.mongo_conn = None
        pass

    @staticmethod
    def prototype_mongo_connector(ip='127.0.01', port=27017, db_name='test', coll_name='test'):
        return MongoConnector(
            uri='mongodb://' + ip + ':' + str(port) + '/admin',
            db_name=db_name,
            coll_name=coll_name,
            fork=True
        )

    def singleton_mongo_connector(self, ip='127.0.01', port=27017, db_name='test', coll_name='test'):
        if self.mongo_conn is None:
            self.mongo_conn = MongoConnector(
                uri='mongodb://' + ip + ':' + str(port) + '/admin',
                db_name=db_name,
                coll_name=coll_name,
                fork=False
            )
        return self.mongo_conn

    def singleton_redis_connector(self, ip, port, db_name=0):
        if self.redis_conn is None:
            self.redis_conn = RedisConnector(host=ip, port=port, db=db_name).connector
        return self.redis_conn
