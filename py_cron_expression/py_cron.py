from py_cron_expression.validations import *
from py_cron_expression.util import remove_zero, PLATFORMS


class CronJobExpression:
    """
    # Example of job definition:
    # .---------------- minute (0 - 59)
    # |  .------------- hour (0 - 23)
    # |  |  .---------- day of month (1 - 31)
    # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
    # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7)
    # |  |  |  |  |
    # *  *  *  *  *   command to be executed
    m-59/n  *  *  *  *   command
    """

    def __init__(self):
        self._seconds = None
        self._minutes = None
        self._hours = None
        self._day = None
        self._month = None
        self._year = None

    @date_valid
    def cron_expression(self, **kwargs) -> str:
        """
        :param kwargs: dict
        :return:
        10 20 12 30 4 ? 2020
        S  M  H  D  M W  Y
        """
        time = kwargs['time']
        cancel = kwargs['cancel']
        date, time = time.split("T")
        self._year, self._month, self._day = date.split("-")
        self._hours, self._minutes, self._seconds = time.split(":")
        if cancel:
            return "{} {} {} {} ? {}".format(
                remove_zero(self._minutes),
                remove_zero(self._hours),
                remove_zero(self._day),
                remove_zero(self._month),
                self._year
            )

        return "{} {} {} {} {} ? {}".format(
            remove_zero(self._seconds),
            remove_zero(self._minutes),
            remove_zero(self._hours),
            remove_zero(self._day),
            remove_zero(self._month),
            self._year
        )

    @platform_valid
    @minute_valid
    def minute(self, platform: str, minutes: int = None) -> str:
        """
        :param platform:
        :param minutes:
        :return:
        """

        if not self._minutes and not minutes:
            raise ValueError("Should pass datetime object or minutes value")

        expression = PLATFORMS.get(platform)
        expression_list = expression.split(" ")
        expression_list[0] = f"*/{minutes or remove_zero(self._minutes)}"
        return " ".join(expression_list)

    @platform_valid
    @hour_valid
    def hourly(self, platform: str, hours: int = None) -> str:
        """
        :param platform:
        :param hours:
        :return:
        """

        if not self._hours and not hours:
            raise ValueError("Should pass datetime object or hours value")

        expression = PLATFORMS.get(platform)
        expression_list = expression.split(" ")
        expression_list[1] = f"*/{hours or remove_zero(self._hours)}"
        return " ".join(expression_list)

    @platform_valid
    @hour_valid
    def daily(self, platform: str, hours: int = None) -> str:
        """
        :param platform:
        :param hours:
        :return:
        """
        if not self._hours and not hours:
            raise ValueError("Should pass datetime object or hours value")

        expression = PLATFORMS.get(platform)
        expression_list = expression.split(" ")
        expression_list[0] = "0"
        expression_list[1] = f"{hours or remove_zero(self._hours)}"
        return " ".join(expression_list)
