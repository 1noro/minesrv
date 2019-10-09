#!/usr/bin/python3
import os
import datetime

today_str = datetime.datetime.now().strftime('%Y-%m-%d')
yesterday_str = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
date_str = ''
logs_today = False
files_arr = []

for root, dirs, files in os.walk("logs"):
    files_arr = files

files_arr.sort()
files_arr.pop()

for filename in files_arr:
    if (today_str in filename):
        logs_today = True

if logs_today:
    date_str = today_str
else:
    date_str = yesterday_str

print("## Lastest logs:")

for filename in files_arr:
    if (date_str in filename):
        print(filename)
