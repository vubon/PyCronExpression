"""
A simple data validation
@Since: 02 May, 2020
"""
from datetime import datetime
from typing import Callable
import pytz
from tzlocal import get_localzone_name

from py_cron_expression.util import WEEKS

GET_TIMEZONE = get_localzone_name()

__all__ = [
    "date_valid", "hour_valid", "minute_valid", "platform_valid", "weekly_valid"
]


def date_valid(func: Callable) -> Callable:
    """
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        try:
            time = kwargs['time']
            timezone = kwargs.get('timezone', GET_TIMEZONE)
            cancel = kwargs.get('cancel', None)
            if isinstance(time, int):
                string = datetime.fromtimestamp(time, tz=pytz.timezone(timezone)).strftime('%Y-%m-%dT%H:%M:%S')
                if cancel != 'second':
                    kwargs['cancel'] = False
                kwargs['time'] = string
                return func(*args, **kwargs)
            elif isinstance(time, datetime):
                string = (time.astimezone(tz=pytz.timezone(timezone))).strftime('%Y-%m-%dT%H:%M:%S')
                if cancel != "second":
                    kwargs['cancel'] = False
                kwargs['time'] = string
                return func(*args, **kwargs)
            else:
                raise ValueError(f"Invalid data type {time}")
        except KeyError as key:
            raise KeyError(f"Key name should {key}")

    return wrapper


def hour_valid(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        hours = kwargs.get("hours")
        if hours:
            if hours not in tuple(hour for hour in range(1, 24)):
                raise ValueError("Should give valid hours value")
        return func(*args, **kwargs)

    return wrapper


def minute_valid(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        minutes = kwargs.get("minutes")
        if minutes and minutes not in tuple(hour for hour in range(1, 60)):
            raise ValueError("Should give valid minutes value")
        return func(*args, **kwargs)

    return wrapper


def weekly_valid(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        day = kwargs.get("weekly")
        value = WEEKS.get(day.lower())
        if day and value is None:
            raise ValueError("Should give valid weekly value")
        kwargs["weekly"] = value
        return func(*args, **kwargs)

    return wrapper


def platform_valid(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        platform = kwargs.get("platform")
        if not platform:
            raise KeyError("Should pass platform key")
        if platform not in ('aws', 'linux'):
            raise ValueError("Should use valid platform. Valid platforms are aws or linux")
        return func(*args, **kwargs)

    return wrapper
