from github import Github
from datetime import datetime
from datetime import timedelta, date
import urllib3
import requests
import secrets


from secrets import USERNAME
from secrets import PASSWORD


g = Github(USERNAME,PASSWORD)

repos = g.get_user().get_repos()
for repo in repos:
    print(repo.name)