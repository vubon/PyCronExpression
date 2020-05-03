from py_cron_expression.validations import date_validation


def remove_zero(number: str) -> str:
    """
    :param number:
    :return:
    """
    return number.replace("0", "") if number.startswith("0") else number


class CronJobExpression:
    @staticmethod
    @date_validation
    def cron_expression(*args, **kwargs) -> str:
        """
        :param args: tuple
        :param kwargs: dict
        :return:
        10 20 12 30 4 ? 2020
        S  M  H  D  M W  Y
        """
        time = kwargs['time']
        cancel = kwargs['cancel']
        date, time = time.split("T")
        year, month, day = date.split("-")
        hours, minutes, seconds = time.split(":")
        if cancel:
            return f"{remove_zero(minutes)} {remove_zero(hours)} {remove_zero(day)} {remove_zero(month)} ? {year}"
        return f"{remove_zero(seconds)} {remove_zero(minutes)} {remove_zero(hours)} {remove_zero(day)} {remove_zero(month)} ? {year}"
