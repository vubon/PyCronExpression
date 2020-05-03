import unittest

from py_cron_expression.py_cron import CronJobExpression


class CronTest(unittest.TestCase):

    def setUp(self) -> None:
        self.valid_timestamp = 1588406110
        self.valid_datetime = ''
        self.invalid_data = "This is a invalid data"
        self.cron_job = CronJobExpression()

    def test_valid_timestamp(self):
        response = self.cron_job.cron_expression(time=self.valid_timestamp)
        self.assertEqual(response, "10 55 13 2 5 ? 2020")

    def test_invalid_data(self):
        response = self.cron_job.cron_expression(time=self.invalid_data)
        self.assertEqual(response, 'Invalid data type This is a invalid data')


if __name__ == "__main__":
    unittest.main()
