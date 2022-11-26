#!usr/bin/env python
# -*- coding: utf-8 -*-

import schedule
import time
import datetime

def job1():
    print("job1",datetime.datetime.now())

def job2():
    print("job2",datetime.datetime.now())

def job3():
    print("job3",datetime.datetime.now())


schedule.every(2).seconds.do(job1)  # 関数job1を、2秒毎に実行する
schedule.every(1).minutes.do(job2)  # 関数job2を、1分毎に実行する

schedule.every().minutes.at(":23").do(job3)  # 関数job3を、毎23秒に実行する

print("start",datetime.datetime.now())

while True:
    schedule.run_pending()
    time.sleep(1)
