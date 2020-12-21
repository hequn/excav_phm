#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 20:12
# @Author  : Qun He
# @File    : setup.py
# @Software: PyCharm

from setuptools import setup

setup(
    name="ExcavPHM",  # pypi中的名称，pip或者easy_install安装时使用的名称
    version="1.0",
    author="Qun He",
    author_email="heq27@sany.com.cn",
    description="The PHM task project.",
    license="GPLv3",
    keywords="excavator PHM",
    url="https://ssl.xxx.org/redmine/projects/ExcavPHM",
    packages=['src', 'conf'],  # 需要打包的目录列表

    # 需要安装的依赖
    install_requires=[
        'redis>=3.5.2',
        'pymongo>=3.11.0',
        'configparser>=5.0.1'
    ],

    # 添加这个选项，在windows下Python目录的scripts下生成exe文件
    # 注意：模块与函数之间是冒号:
    entry_points={'console_scripts': [
        'phm_run = src.tasks_entry:main',
    ]},

    # long_description=read('README.md'),
    classifiers=[  # 程序的所属分类列表
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    # 此项需要，否则卸载时报windows error
    zip_safe=False
)
