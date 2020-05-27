## Python Cron Expression

This is a simple library for making cron job expression. 
User need to pass timestamp or datetime object to create cron job expression. 

## Installation
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
| Weekly                               | `Comming`        

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
If you need to convert the cron job expression to other timezone. Please follow the example. 
By default your will get the cron job expression as your local timezone. 
```python
from datetime import datetime
from py_cron_expression import CronJobExpression
cron_job = CronJobExpression()

timestamp = int(datetime.now().timestamp())
res = cron_job.cron_expression(time=timestamp, timezone='Asia/Dhaka')
print(res)
# Output 
# 10 55 13 2 5 ? 2020
```
Below features will give you two types of cron expression 1. AWS platform and 2. Linux. 
Both platforms are not supported second. So by default removed the second from the expression
#### Minute
```python
from py_cron_expression import CronJobExpression
cron = CronJobExpression()
minute = cron.minute(platform="aws", minutes=10)
print(minute)
# */10 * * * ? * 
# Every 10 minutes starting at :00 minute after the hour
minute = cron.minute(platform="linux", minutes=10)
print(minute)
# */10 * * * *
# Every 10 minutes starting at :00 minute after the hour
```
#### Hourly
```Python
from py_cron_expression import CronJobExpression
cron = CronJobExpression()
hourly = cron.hourly(platform="aws", minutes=1)
print(hourly)
# * */1 * * ? *
# Every hour starting at 00am
hourly = cron.hourly(platform="linux", minutes=1)
print(hourly)
# * */1 * * *
# Every hour starting at 00am
```
#### Daily 
```Python
from py_cron_expression import CronJobExpression
cron = CronJobExpression()
daily = cron.daily(platform="aws", minutes=1)
print(daily)
# 0 1 * * ? *
# At 01:00:00am every day
daily = cron.daily(platform="linux", minutes=1)
print(daily)
# 0 1 * * *
# At 01:00:00am every day
```