#!/usr/bin/python3
import os
import gzip
# import datetime

# today_str = datetime.datetime.now().strftime('%Y-%m-%d')
date_str = ''
logs_today = False
files_arr = []

for root, dirs, files in os.walk("logs"):
    files_arr = files

files_arr.sort()
files_arr.pop() # delete the las element (latest.log)

date_str = files_arr[-1][:10]

print("## Last day logs ("+date_str+"):")

for filename in files_arr:
    if (date_str in filename):
        # print("## Reading 'logs/"+filename+"'")
        f = gzip.open('logs/'+filename, 'rb')
        file_content = f.read()
        f.close()
        print(file_content.decode('utf-8'))

# f = gzip.open('logs/2019-10-09-6.log.gz', 'rb')
# file_content = f.read()
# f.close()
# print("## Reading 'logs/2019-10-09-6.log.gz'")
# print(file_content.decode('utf-8'))
