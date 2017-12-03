from __future__ import absolute_import
import sys
from datetime import date, datetime, timedelta
from password import *
from redminelib import Redmine
redmine = Redmine(redmine_url, key=api_key)

# To request with time filter redmine date style
def today_date_string():
    today = date.today()
    return today.strftime("%Y-%m-%d")

# To request with time filter redmine date style
def seven_days_date_string():
    today = date.today()
    seven_days_before = today - timedelta(7)
    return seven_days_before.strftime("%Y-%m-%d")

# An error may be occur
try:
    today_str = today_date_string()
    seven_day_str = seven_days_date_string()
    print(today_str)
    print(seven_day_str)
    issues = redmine.issue.filter(
        created_on='><'+seven_day_str+'|'+today_str
    )
    for issue in issues:
        print(issue.author)
except (ResourceNotFoundError):
    print ('Not found')
