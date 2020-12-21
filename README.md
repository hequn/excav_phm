Excavator PHM Project
===============

A framework for all of the phm tasks.

Current works
----------------

__Battery Low__:

| FIle       | Description |
|:----------:| ----------- |
| [battery_voltage_low_worker](src/battery_voltage_low_task/battery_voltage_low_worker.py) | battery will have low voltage so give the warn to users |

Contributing
------------
When an implementation is added or modified, please review the following guidelines:

##### Init Paths
Take notice of the [_init_paths.py](src/_init_paths.py) file. If you py file want to import cross package func or class, you must add a right settled _init_paths.py file in order to have a right PYTHONPATH.

##### Logs
All logfiles should be located in excav_phm/logs dir. 
* task_executor.log: refers to [tasks_executor](src/tasks_executor.py) info.
* xxx_task.xxx_worker.log: refers to the info that task worker instances have, except ```execute method```.
* multi_task_workers.log: refers to the info that shared logger output in multiprocess, only in the ```execute method```.
* mongo.log: refers to [mongo_utils](src/utils/mongo_utils.py).
* add you own things.

##### Conf
Config files should be located in excav_phmc/conf dir.
* baseConfig.ini: base params are set in this file.
* add you own things.

##### Docstrings
Add module level description in form of a docstring with links to corresponding references or other useful information.

Add "Examples in Python ecosystem" section if you know some. It shows how patterns could be applied to real-world problems.

##### Update README
When everything else is done - update corresponding part of README.

## Contributing via issue triage [![Open Source Helpers](https://www.codetriage.com/faif/python-patterns/badges/users.svg)](https://www.codetriage.com/faif/python-patterns)

You can triage issues and pull requests which may include reproducing bug reports or asking for vital information, such as version numbers or reproduction instructions. If you would like to start triaging issues, one easy way to get started is to [subscribe to python-patterns on CodeTriage](https://www.codetriage.com/faif/python-patterns).
