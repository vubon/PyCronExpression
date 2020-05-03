## Python Cron Expression

This is a simple library for making cron job expression. 
User need to pass timestamp or datetime object to create cron job expression. 

## Installation
```shell script
pip install PyCronExpression
```

## Example 
```python
from datetime import datetime
from py_cron_expression.py_cron import CronJobExpression
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
