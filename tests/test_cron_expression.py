import datetime
import unittest

from py_cron_expression import CronJobExpression


class CronTest(unittest.TestCase):

    def setUp(self) -> None:
        self.valid_timestamp = 1588406110
        self.valid_datetime = datetime.datetime.now() - datetime.timedelta(hours=datetime.datetime.now().hour)
        self.invalid_data = "This is a invalid data"
        self.cron = CronJobExpression()

    def test_valid_timestamp(self):
        response = self.cron.cron_expression(time=self.valid_timestamp)
        self.assertEqual(response, "10 55 13 2 5 ? 2020")

    def test_valid_datetime(self):
        res = self.cron.cron_expression(time=self.valid_datetime)
        print(res)

    def test_valid_omit_second(self):
        res = self.cron.cron_expression(time=self.valid_timestamp, cancel='second')
        self.assertEqual(res, "55 13 2 5 ? 2020")

    def test_invalid_data(self):
        self.assertRaises(ValueError, lambda: self.cron.cron_expression(time=self.invalid_data))

    def test_invalid_key_name(self):
        self.assertRaises(KeyError, lambda: self.cron.cron_expression(times=self.valid_timestamp))
