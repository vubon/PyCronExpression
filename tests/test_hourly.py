import unittest

from py_cron_expression import CronJobExpression


class TestMinute(unittest.TestCase):

    def setUp(self) -> None:
        self.cron = CronJobExpression()
        self.valid = {"platform": "aws", "hours": 1}
        self.invalid_platform = {"platform": "awss", "hours": 1}
        self.invalid_hours = {"platform": "aws", "hours": -1}

    def test_valid(self):
        res = self.cron.hourly(**self.valid)
        self.assertEqual(res, '* */1 * * ? *')

    def test_invalid_platform(self):
        self.assertRaises(ValueError, lambda: self.cron.hourly(**self.invalid_platform))

    def test_invalid_hours(self):
        self.assertRaises(ValueError, lambda: self.cron.hourly(**self.invalid_hours))

    def test_without_hours(self):
        self.assertRaises(ValueError, lambda: self.cron.hourly(platform='aws'))
