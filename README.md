# Python Cron Expression
[![PyPI version](https://badge.fury.io/py/PyCronExpression.svg)](https://badge.fury.io/py/PyCronExpression)
![Coverage](https://raw.githubusercontent.com/vubon/PyCronExpression/master/docs/coverage.svg)
[![GitHub version](https://badge.fury.io/gh/vubon%2FPyCronExpression.svg)](https://badge.fury.io/gh/vubon%2FPyCronExpression)

## Introduction
This is a simple library for making cron job expression. 
User need to pass timestamp or datetime object to create cron job expression. 

## Quickstart
### Installation
Install from pypi: 
```shell script
pip install PyCronExpression
```

##### Feature List

| Name                                 | status     
| ---                                  | ---        
| Timestamp or datetime object         | `done`       
| Minute                               | `done`      
| Hourly                               | `done`       
| Daily                                | `Done` 
| Weekly                               | `done`        

## Example 

#### Timestamp or datetime object
```python
from datetime import datetime
from py_cron_expression import CronJobExpression
cron_job = CronJobExpression()

timestamp = int(datetime.now().timestamp())
res = cron_job.cron_expression(time=timestamp)
print(res)
# Output 
# 10 55 13 2 5 ? 2020

# If you want to remove second from in your cron job expression. 
# Then you need to add cancel='second'
# example
cron_job.cron_expression(time=timestamp, cancel='second')
# Output 
# 55 13 2 5 ? 2020
```
To learn more [Documentation](./docs/guide.md).

## Changelog
See [Changelog](CHANGELOG.md)

## License
MIT