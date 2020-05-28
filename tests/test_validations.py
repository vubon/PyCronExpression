import unittest
from datetime import datetime
from py_cron_expression.validations import (
    date_valid, hour_valid, minute_valid, weekly_valid, platform_valid
)


class TestValidations(unittest.TestCase):
    def test_date_valid_positive_timestamp(self):
        @date_valid
        def test_function(time, timezone, cancel):
            return True

        # Positive case: Valid timestamp
        timestamp = 1591059200  # May 3, 2020, 00:00:00 in seconds
        self.assertTrue(test_function(time=timestamp, timezone="Asia/Bangkok", cancel=False))

    def test_date_valid_positive_datetime(self):
        @date_valid
        def test_function(time, timezone, cancel):
            return True

        # Positive case: Valid datetime object
        dt = datetime(2020, 5, 3, 12, 0, 0)
        self.assertTrue(test_function(time=dt, timezone="UTC", cancel=False))

    def test_date_valid_negative_invalid_type(self):
        @date_valid
        def test_function(time, timezone, cancel):
            return True

        # Negative case: Invalid data type
        with self.assertRaises(ValueError):
            self.assertFalse(test_function(time="2020-05-03T12:00:00", timezone="UTC", cancel=False))

    def test_hour_valid_positive(self):
        @hour_valid
        def test_function(hours):
            return True

        # Positive case: Valid hour value
        self.assertTrue(test_function(hours=12))

    def test_hour_valid_negative_invalid_hour(self):
        @hour_valid
        def test_function(hours):
            return True

        # Negative case: Invalid hour value
        with self.assertRaises(ValueError):
            self.assertFalse(test_function(hours=25))

    def test_minute_valid_positive(self):
        @minute_valid
        def test_function(minutes):
            return True

        # Positive case: Valid minute value
        self.assertTrue(test_function(minutes=30))

    def test_minute_valid_negative_invalid_minute(self):
        @minute_valid
        def test_function(minutes):
            return True

        # Negative case: Invalid minute value
        with self.assertRaises(ValueError):
            self.assertFalse(test_function(minutes=61))

    def test_weekly_valid_positive(self):
        @weekly_valid
        def test_function(weekly):
            return True

        # Positive case: Valid day of the week
        self.assertTrue(test_function(weekly="friday"))

    def test_weekly_valid_negative_invalid_day(self):
        @weekly_valid
        def test_function(weekly):
            return True

        # Negative case: Invalid day of the week
        with self.assertRaises(ValueError):
            self.assertFalse(test_function(weekly="Noday"))

    def test_platform_valid_positive(self):
        @platform_valid
        def test_function(platform):
            return True

        # Positive case: Valid platform
        self.assertTrue(test_function(platform="aws"))
        self.assertTrue(test_function(platform="linux"))

    def test_platform_valid_negative_invalid_platform(self):
        @platform_valid
        def test_function(platform):
            return True

        # Negative case: Invalid platform
        with self.assertRaises(ValueError):
            self.assertFalse(test_function(platform="invalid"))

    def test_platform_valid_negative_missing_platform(self):
        @platform_valid
        def test_function(platform):
            return True

        # Negative case: Missing platform
        with self.assertRaises(KeyError):
            self.assertFalse(test_function())
