import unittest

from py_cron_expression import CronJobExpression


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
        self.assertRaises(ValueError, lambda: self.cron_job.cron_expression(time=self.invalid_data))


if __name__ == "__main__":
    unittest.main()
