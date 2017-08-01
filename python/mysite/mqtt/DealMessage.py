#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'weishijian'
'''
这个文件用来处理收到的消息.

在此项目中,是用来处理mqtt的消息的.
'''


sysID = "0150"



from M2Crypto.EVP import Cipher

def encrypt_3des(key, text):
    encryptor = Cipher(alg='des_ede3_ecb', key=key, op=1, iv='\0'*16)
    s = encryptor.update(text)
    return s+ encryptor.final()

def decrypt_3des(key, text):
    decryptor = Cipher(alg='des_ede3_ecb', key=key, op=0, iv='\0'*16)
    s= decryptor.update(text)
    return s + decryptor.final()
key = "12345678abcdefgh12345678"

devices = {}


import time
# Utility module
from binascii import unhexlify as unhex

from ctypes import *
import os
import struct
import json
# 用于进行http访问
import urllib2
import codecs, binascii, base64
import threading

import MySocket

import dealDB

mutex = threading.Lock()

def dealData(topicString, string, lenOfString):
    """

    Args:
        string

    Returns:

    """

    # create a  C type string  ( char* )
    if mutex.acquire(1):
        try:

#            print "string = %s" %(string)
#            print topicString
#            print "topicString split[2] = %s" %(topicString.split('/')[2])

            MAC = (topicString.split('/')[2]).decode('utf-8')

            string = base64.b64decode(string)

            str = decrypt_3des(key, string)

            import json

            jsonDecode = json.loads(str)

            optCode = jsonDecode["optCode"]
            print optCode
            if optCode == "heart" or optCode == "beat":
                payLoad = {}
                payLoad["optCode"] = "0081"
                payLoad["timeOut"] = str(int(time.time() * 1000))
                strPayLoad = json.dumps(payLoad)
                encrypt_text = encrypt_3des(key, strPayLoad)
                b64Str = base64.b64encode(encrypt_text)

                ret_topic_str = "isockets/Topic/" + MAC
                commandList = ["Publish", ret_topic_str, b64Str, len(b64Str)]
                MySocket.commandArray.append(commandList)
                MySocket.socketSemaphore.release()

            elif optCode == "0050":
                pass
            elif optCode == "0030":
                devArray = jsonDecode["devArray"]
                DevID = devArray[0]["devID"]
                print "DevID = %s" % (DevID)
                deviceInfoDic = {}
                global devices
                if DevID in devices.keys():
                    deviceInfoDic = devices[DevID]
                else:
                    deviceInfoDic = {}


                deviceInfoDic["devID"] = DevID
                # deviceInfoDic["heartime"] = jsonDecode['timeOut']
                deviceInfoDic["heartime"] = time.time() * 1000

                print "deviceInfoDic = ", deviceInfoDic

                senmap = {}
                if "senmap" in deviceInfoDic.keys():
                    senmap = deviceInfoDic["senmap"]
                else:
                    senmap = {}


                senArray = devArray[0]['senArray']
                print 'senArray', senArray

                print "           "

                for senArrayItem in senArray:
                    senID = senArrayItem["senID"]
                    senType = senArrayItem["senType"]
                    errCode = jsonDecode["errCode"]

                    senmapItem = {}
                    if senID in senmap.keys():
                        senmapItem = senmap[senID]
                    else:
                        senmapItem = {}


                    senmapItem["senID"] = senID
                    senmapItem["sensorType"] = senType
                    senmapItem["sentime"] = time.time() * 1000
                    result = ""
                    if errCode == "9999":
                        result = "success"
                    elif errCode == "1111":
                        result = "circuit power off"
                    elif errCode == "0000":
                        result = "meter power off"
                    else:
                        result = "failed"
                    senmapItem["result"] = result

                    print "senmapItem = ", senmapItem
                    senmapParaArray = []
                    if "list" in senmapItem:
                        senmapParaArray = senmapItem["list"]
                    else:
                        senmapParaArray = []

                    print "senmapParaArray = ", senmapParaArray

                    paraArray = senArrayItem["paramArray"]  # get paramArray from json
                    lenOfParaArray = len(paraArray)

                    for paraArrayItem in paraArray:
                        senmapParaArray.append(paraArrayItem)
                    senmapItem["list"] = senmapParaArray
                    senmap[senID] = senmapItem

                deviceInfoDic["senmap"] = senmap
                devices[DevID] = deviceInfoDic

                print " -------------------"
                print "devices = ", json.dumps(devices)

            else:
                pass


        except Exception as e:
            print "exception = %s" % e
        finally:
            mutex.release()


def getAllDevice():
    global devices
    return devices
