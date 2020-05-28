import unittest

from py_cron_expression import CronJobExpression


class TestMinute(unittest.TestCase):

    def setUp(self) -> None:
        self.cron = CronJobExpression()
        self.valid = {"platform": "aws", "minutes": 1}
        self.invalid_platform = {"platform": "awss", "minutes": 1}
        self.invalid_key = {"platforms": "aws", "minutes": 1}
        self.invalid_minutes = {"platform": "aws", "minutes": -1}

    def test_valid(self):
        res = self.cron.minute(**self.valid)
        self.assertEqual(res, '*/1 * * * ? *')

    def test_invalid_platform(self):
        self.assertRaises(ValueError, lambda: self.cron.minute(**self.invalid_platform))

    def test_invalid_minutes(self):
        self.assertRaises(ValueError, lambda: self.cron.minute(**self.invalid_minutes))

    def test_without_minutes(self):
        self.assertRaises(ValueError, lambda: self.cron.minute(platform='aws'))

    def test_invalid_key(self):
        self.assertRaises(KeyError, lambda: self.cron.minute(**self.invalid_key))
