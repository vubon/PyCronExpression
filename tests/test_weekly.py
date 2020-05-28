import unittest

from py_cron_expression import CronJobExpression


class TestWeekly(unittest.TestCase):

    def setUp(self) -> None:
        self.cron = CronJobExpression()
        self.valid = {"platform": "linux", "hours": 1, "minutes": 10, "weekly": "sunday"}

    def test_valid(self):
        result = self.cron.weekly(**self.valid)
        self.assertEqual(result, "10 1 * * 0")

