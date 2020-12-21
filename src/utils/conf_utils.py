#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:51
# @Author  : Qun He
# @File    : conf_utils.py
# @Software: PyCharm

import configparser
import os
from path_holder import PathHolder


class OperationalError(Exception):
    """Operation error."""


class Dictionary(dict):
    """
    Custom dict.
    The below func can't be used for in multiprocess mode, a NoneType error will be raised and very difficult to find.
        def __getattr__(self, key):
        return self.get(key, None)
    """

    def getattr(self, key):
        return self.get(key, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Config:
    def __init__(self, file_name="test", cfg=None):
        """
        @param file_name: file name without extension.
        @param cfg: configuration file path.
        """
        env = {}
        for key, value in os.environ.items():
            if key.startswith("TEST_"):
                env[key] = value

        config = configparser.ConfigParser(env)

        if cfg:
            config.read(cfg)
        else:
            config.read(os.path.join(PathHolder.CONF_PATH, "%s.ini" % file_name))

        for section in config.sections():
            setattr(self, section, Dictionary())
            for name, raw_value in config.items(section):
                try:
                    # Ugly fix to avoid '0' and '1' to be parsed as a boolean value.
                    # We raise an exception to goto fail^w parse it as integer.
                    if config.get(section, name) in ["0", "1"]:
                        raise ValueError

                    value = config.getboolean(section, name)
                except ValueError:
                    try:
                        value = config.getint(section, name)
                    except ValueError:
                        value = config.get(section, name)

                setattr(getattr(self, section), name, value)

    def get(self, section):
        """Get option.
        @param section: section to fetch.
        @return: option value.
        """
        try:
            return getattr(self, section)
        except AttributeError as e:
            raise OperationalError("Option %s is not found in configuration, error: %s" % (section, e))
