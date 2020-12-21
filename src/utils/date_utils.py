#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 20:12
# @Author  : Qun He
# @File    : date_utils.py
# @Software: PyCharm
import datetime
import time

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
TIME_FORMAT = "%H:%M:%S"


class DateHelper:
    """
    DateHelper.
    """
    @staticmethod
    def cur_millis() -> int:
        """
        Current milliseconds.
        :return: current milliseconds
        """
        return int(time.time() * 1000)

    @staticmethod
    def cur_seconds() -> int:
        """
        Current seconds.
        :return: current seconds
        """
        return int(time.time())

    @staticmethod
    def cur_datetime_str() -> str:
        """
        Current date with formatting %Y-%m-%d %H:%M:%S.
        :return: cur date with formatting %Y-%m-%d %H:%M:%S str
        """
        return datetime.datetime.strftime(datetime.datetime.now(), DATETIME_FORMAT)

    @staticmethod
    def cur_date() -> datetime.date:
        """
        Current date with formatting %Y-%m-%d.
        :return: cur date with formatting %Y-%m-%d
        """
        return datetime.date.today()

    @staticmethod
    def cur_time_str() -> str:
        """
        Current time with formatting %H:%M:%S.
        :return: cur time with formatting %H:%M:%S str
        """
        return time.strftime(TIME_FORMAT)

    @staticmethod
    def seconds_to_datetime(seconds) -> str:
        """
        Seconds_to_datetime "%Y-%m-%d %H:%M:%S"
        :param seconds: seconds.
        :return: datetime str
        """
        return time.strftime(DATETIME_FORMAT, time.localtime(seconds))

    @staticmethod
    def millis_to_datetime(millis) -> str:
        """
        Millis_to_datetime "%Y-%m-%d %H:%M:%S"
        :param millis: milliseconds.
        :return: datetime str
        """
        return time.strftime(DATETIME_FORMAT, time.localtime(millis // 1000))

    @staticmethod
    def datetime_to_millis(date_time_str) -> int:
        """
        "%Y-%m-%d %H:%M:%S" str to milliseconds
        :param date_time_str: "%Y-%m-%d %H:%M:%S" .
        :return: milliseconds
        """
        str_format = time.strptime(date_time_str, DATETIME_FORMAT)
        return int(time.mktime(str_format)) * 1000

    @staticmethod
    def datetime_to_seconds(date_time_str) -> int:
        """
        "%Y-%m-%d %H:%M:%S" to seconds.
        :param date_time_str: "%Y-%m-%d %H:%M:%S" .
        :return: seconds
        """
        str_format = time.strptime(date_time_str, DATETIME_FORMAT)
        return int(time.mktime(str_format))

    @staticmethod
    def cur_year() -> int:
        """
        Current year.
        :return: current year
        """
        return datetime.datetime.now().year

    @staticmethod
    def cur_month() -> int:
        """
        Current month.
        :return: current month
        """
        return datetime.datetime.now().month

    @staticmethod
    def cur_day() -> int:
        """
        Current day.
        :return: current day
        """
        return datetime.datetime.now().day

    @staticmethod
    def cur_hour() -> int:
        """
        Current hour.
        :return: current hour
        """
        return datetime.datetime.now().hour

    @staticmethod
    def cur_minute() -> int:
        """
        Current minute.
        :return: current minute
        """
        return datetime.datetime.now().minute

    @staticmethod
    def cur_second() -> int:
        """
        Current second.
        :return: current second
        """
        return datetime.datetime.now().second

    @staticmethod
    def cur_week() -> int:
        """
        Week day range from 1 - 7.
        :return: current week day
        """
        return datetime.datetime.now().weekday() + 1

    @staticmethod
    def now_days_ago(days) -> str:
        """
        Days ago, today base.
        :param days: days.
        :return: "%Y-%m-%d %H:%M:%S" str
        """
        days_ago_time = datetime.datetime.now() - datetime.timedelta(days=days)
        return time.strftime(DATETIME_FORMAT, days_ago_time.timetuple())

    @staticmethod
    def now_days_after(days) -> str:
        """
        Days after, today base.
        :param days: days.
        :return: "%Y-%m-%d %H:%M:%S" str
        """
        days_after_time = datetime.datetime.now() + datetime.timedelta(days=days)
        return time.strftime(DATETIME_FORMAT, days_after_time.timetuple())

    @staticmethod
    def someday_days_ago(day_time_str, days) -> str:
        """
        Days ago, day_time_str base.
        :param day_time_str: original date str.
        :param days: days.
        :return: target day str
        """
        days_ago_time = datetime.datetime.strptime(day_time_str, DATETIME_FORMAT) - datetime.timedelta(days=days)
        return time.strftime(DATETIME_FORMAT, days_ago_time.timetuple())

    @staticmethod
    def someday_days_after(day_time_str, days) -> str:
        """
        Days after, day_time_str base
        :param day_time_str:  original date str.
        :param days:  days.
        :return: target day str
        """
        days_after_time = datetime.datetime.strptime(day_time_str, DATETIME_FORMAT) + datetime.timedelta(days=days)
        return time.strftime(DATETIME_FORMAT, days_after_time.timetuple())
