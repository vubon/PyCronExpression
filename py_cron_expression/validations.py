"""
A simple data validation
@Since: 02 May, 2020
"""
from datetime import datetime


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
            cancel = kwargs.get('cancel', None)
            if isinstance(time, int):
                string = datetime.fromtimestamp(time).isoformat()
                if cancel == 'second':
                    kwargs['cancel'] = True
                else:
                    kwargs['cancel'] = False
                kwargs['time'] = string
                return func(*args, **kwargs)
            elif isinstance(time, datetime):
                string = time.isoformat().split(".")[0]
                if cancel == "second":
                    kwargs['cancel'] = True
                else:
                    kwargs['cancel'] = False
                kwargs['time'] = string
                return func(*args, **kwargs)
            else:
                raise ValueError(f"Invalid data type {time}")
        except KeyError as err:
            raise KeyError(f"Key name should {err}")

    return wrapper
