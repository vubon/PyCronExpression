"""
@since: 26 May 2020

# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
Linux platform cron job definition
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7)
# |  |  |  |  |
# *  *  *  *  *

AWS platform cron job definition
# .---------------------- minute (0 - 59)
# |  .------------------- hour (0 - 23)
# |  |   .---------------- day of month (1 - 31)
# |  |  |   .------------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |   .---------- day of week (0 - 6) (Sunday=0 or 7)
# |  |  |  |  |  .-------- year
# |  |  |  |  | |
# *  *  *  *  ? *
aws docs link: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
"""

PLATFORMS = {
    "linux": "* * * * *",
    "aws": "* * * * ? *"
}

WEEKS = {
    "sunday": "0",
    "monday": "1",
    "tuesday": "2",
    "wednesday": "3",
    "thursday": "4",
    "friday": "5",
    "saturday": "6"
}


def remove_zero(number: str) -> str:
    """
    :param number:
    :return:
    """
    if number.startswith("0") and number.endswith("0"):
        return "0"
    elif number.startswith("0"):
        return number.replace("0", "")
    else:
        return number
