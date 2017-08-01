#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'weishijian'
'''
与数据库交互
'''

import sqlite3

def getDeviceInfo(deviceID):
    """

    Args:
        deviceID

    Returns:

    """
    results = []

    conn = sqlite3.connect('../CAM_WEB_SETUP/db.sqlite3')
    cursor = conn.cursor()
    sql = 'select location, label from CAM_devices where devicesId = "%s";' % deviceID
    cursor.execute(sql)
    deviceInfo = cursor.fetchall()
    print deviceInfo



    return deviceInfo

def getUserDevicesInfo(user):
    """

    Args:
        user

    Returns:

    """

    results = []

    conn = sqlite3.connect('../CAM_WEB_SETUP/db.sqlite3')
    cursor = conn.cursor()
    sql = 'select id from CAM_users where user = "%s";' % user
    cursor.execute(sql)
    userRet = cursor.fetchall()
    print userRet
    print len(userRet)

    print userRet[0][0]

    sql = 'select devices_id from CAM_users_devices where users_id = "%s";' % userRet[0][0]
    cursor.execute(sql)
    user_Devices = cursor.fetchall()
    print user_Devices
    for device in user_Devices:
        deviceId = device[0]
        sql = 'select location, label, devicesId from CAM_devices where id = "%s";' % deviceId
        cursor.execute(sql)
        deviceInfo = cursor.fetchall()
        print deviceInfo
        dic = {}
        dic['location'] = deviceInfo[0][0]
        dic['label'] = deviceInfo[0][1]
        dic['devID'] = deviceInfo[0][2]
        results.append(dic)

    print results
    return results
def getUserInfo(user):
    results = []

    conn = sqlite3.connect('../CAM_WEB_SETUP/db.sqlite3')
    cursor = conn.cursor()
    sql = 'select pwd from CAM_users where user = "%s";' % user
    cursor.execute(sql)
    userRet = cursor.fetchall()
    print userRet
    print len(userRet)
    i = len(userRet)
    if i < 1:
        return "no User"
    else:
        return userRet[0][0]




# conn = sqlite3.connect("../CAM_WEB_SETUP/db.sqlite3")
#
# c = conn.cursor()
#
# c.execute('''SELECT name FROM sqlite_master WHERE type='table';''')
#
# a = c.fetchall()
#
# print a
#
# c.execute('Select * from CAM_users;')
#
# b = c.fetchall()
#
# print b
#
#
# c.execute('select * from CAM_users_devices;')
#
# d = c.fetchall()
# print d
#
#
# c.execute('select * from CAM_devices where id = 9;')
#
# e = c.fetchall()
# print e
#
#
#
# c.execute('PRAGMA table_info(CAM_users_devices);')
#
# f = c.fetchall()
# print f
#
#
# c.execute('pragma table_info(CAM_users);')
# g = c.fetchall()
# print g
#
# c.execute('pragma table_info(CAM_devices);')
# h = c.fetchall()
# print h
#
# getUserDevicesInfo('user1')
#
#
# c.execute("select location, label from CAM_devices where devicesId = '30CD3A9A24D90A26C3F8494A6ED84F75';")
# dd = c.fetchall()
# print dd
