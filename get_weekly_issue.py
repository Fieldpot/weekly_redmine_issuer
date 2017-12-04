from __future__ import absolute_import
import sys
import requests
import json
from collections import Counter
from datetime import date, datetime, timedelta
from utils import *
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

# Return issuer list
def listup_issuer():
    issuer_list = []
    # An error may be occur
    try:
        today_str = today_date_string()
        seven_day_str = seven_days_date_string()
        issues = redmine.issue.filter(
            # created_on = '><2012-03-01|2012-03-07'
            created_on='><'+seven_day_str+'|'+today_str
        )
        for issue in issues:
            issuer_list.append(str(issue.author))
        return issuer_list
    except (ResourceNotFoundError):
        print ('Not found')
        return null 

issuer_list_unsorted = listup_issuer()
counter = Counter(issuer_list_unsorted)
print(counter)
requests.post(
    slack_webhook_url, data = json.dumps({
        'text': str(counter.most_common()), # 投稿するテキスト
        'username': u'me', # 投稿のユーザー名
        'icon_emoji': u':shipit:', # 投稿のプロフィール画像に入れる絵文字
        'link_names': 1, # メンションを有効にする
}))
