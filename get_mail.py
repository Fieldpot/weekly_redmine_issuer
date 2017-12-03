from __future__ import absolute_import
import sys
from password import *
from redminelib import Redmine
redmine = Redmine(redmine_url, key=api_key)

try:
    user = redmine.user.get('current')
    print(user.mail)
except (ResourceNotFoundError):
    print ('Not found')
