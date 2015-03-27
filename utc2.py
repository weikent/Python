#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2014-09-09 15:08:11 +0000 1410275291000

#[python]
#设a为字符串
import time
#a = "2011-09-28 10:00:00"
#a = "1970-01-01 00:00:00"
a = "2014-09-09 15:08:11"

#中间过程，一般都需要将字符串转化为时间数组
print time.strptime(a,'%Y-%m-%d %H:%M:%S')
#time.struct_time(tm_year=2011, tm_mon=9, tm_mday=27, tm_hour=10, tm_min=50, tm_sec=0, tm_wday=1, tm_yday=270, tm_isdst=-1)
# print time.struct_time.tm_year
# print time.struct_time.tm_mon
# print time.struct_time.tm_mday
# print time.struct_time.tm_hour

#将"2011-09-28 10:00:00"转化为时间戳
print time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
#1317091800.0

#将时间戳转化为localtime
#x = time.localtime(1317091800.0)
x = time.localtime(1410275291)
print time.strftime('%Y-%m-%d %H:%M:%S',x)

#2011-09-27 10:50:00
#[/python]








import datetime
import time
dateC=datetime.datetime(1970,1,1,0,0,0)
timestamp=time.mktime(dateC.timetuple())
print timestamp


import datetime
import time
ltime=time.localtime(0)
timeStr=time.strftime("%Y-%m-%d %H:%M:%S", ltime)
print timeStr



# print "time.time()", time.time()
# print "time.localtime(0)", time.localtime(0)
# print "time.gmtime(0)",time.gmtime(0)