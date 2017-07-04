#!/usr/bin/python3
# coding=utf-8

import time
import datetime

"""
这是多行注释
"""
# 单行注释


def showdate(scound):
    starttime = datetime.datetime.now()
    time.sleep(scound)
    endtime = datetime.datetime.now()
    print(endtime - starttime)

showdate(0.5)