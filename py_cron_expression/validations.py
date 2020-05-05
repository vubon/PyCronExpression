"""
A simple data validation
@Since: 02 May, 2020
"""
from datetime import datetime
import pytz
from tzlocal import get_localzone

GET_TIMEZONE = get_localzone()


def date_validation(func):
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
            timezone = kwargs.get('timezone', GET_TIMEZONE.zone)
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
        except KeyError as err:
            raise KeyError(f"Key name should {err}")

    return wrapper
