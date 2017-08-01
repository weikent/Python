#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'weishijian'

'''
这个文件用来处理所有的socket事务. 创建socket,发送,接收,等.
'''

import select
import socket
import Queue
import time
import os
import sys

import MQTT_Package
import DealMessage
import struct
import threading
import platform

isServerConnected = False   #判断是否与服务器连接成功

isMQTTConnected = False
isMQTTSubscribe = False

connectIdentifier = platform.uname()[0] + platform.uname()[3] + "server"

SUBSCRIBE_TOPIC = "isockets/Device/#"

socketID = -1

serverIP = 'mosquitto.org'
#serverIP = '85.119.83.194'
serverPort = 1883



commandArray = []

socketSemaphore = threading.Semaphore(0)

sendDic = []


# def setServerInfo(ip, port):
#     global serverPort
#     global serverIP
#     serverPort = port
#     serverIP = ip


def isCreated():
    return socketID != -1


def createSocket():
    global socketID
    socketID = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socketID.setblocking(False)

    if socketID < 0:
        return -1
    print "socketID = %s" %(socketID)
    return socketID


def closeSocket():
    isMQTTConnected = False
    isMQTTSubscribe = False
    global socketID
    if socketID > 0:
        socketID.close()
    socketID = -1




def readLoop():
    while True:
        if not isCreated():
            time.sleep(1)
            continue
        else:
            # do nothing.
            pass

        if not isServerConnected:
            time.sleep(1)
            continue
        else:
            pass


        global socketID
        print "socketID = %s" %(socketID)
        inputs = [socketID]
        outputs = []
        while True:

            if not isCreated():
                print "socket is colsed, so break to upper loop"
                break;
            else:
                pass

            print "start select"
            readable , writeable, exceptional = select.select(inputs, outputs, inputs, 60)

            if not readable:
                print "time out"
                global isServerConnected
                global isMQTTConnected
                global isMQTTSubscribe
                global socketID
                closeSocket()
                print "close Socket"
                isServerConnected = False
                isMQTTSubscribe = False
                isMQTTConnected = False
                socketSemaphore.release()
                break
            for s in readable:
                if s is socketID:
                    print "get data"
                    buf = bytearray(b" " * 1)
                    ret = s.recv_into(buf, 1)
                    if ret > 0:
                        if buf[0] == MQTT_Package.MESSAGE_TYPE_CONNACK:
                            print "got mqtt connack"
                            # buf = bytearray(b" " * 3)
                            # ret = s.recv_into(buf, 3)
                            # if ret > 0:
                            #     if buf[2] == 0:
                            #         print "connack is accepted"
                            #         global  isMQTTConnected
                            #         isMQTTConnected = True
                            #         print isMQTTConnected
                            #         socketSemaphore.release()
                            #     else:
                            #         print "connack is refused"
                            # else:
                            #     print tool.get_head_info()
                            #     print "should close socket"
                            #     closeSocket()
                            #     break
                            global isMQTTConnected
                            isMQTTConnected = True
                            socketSemaphore.release()

                            break
                        elif buf[0] == MQTT_Package.MESSAGE_TYPE_SUBACK:
                            print "got mqtt suback"
                            global  isMQTTSubscribe
                            isMQTTSubscribe = True
                            socketSemaphore.release()
                            break
                        elif buf[0] == MQTT_Package.MESSAGE_TYPE_PINGRESP:
                            print "got mqtt pingresp"
                            break
                        elif buf[0] == MQTT_Package.MESSAGE_TYPE_PUBLISH:
                            # this is a message
                            print "this is a message"
                            multiplier = 1
                            remainingLength = 0

                            count = 0
                            while True:
                                buf = bytearray(b" " * 1)

                                ret = s.recv_into(buf, 1)
                                print "recv byte is %02x" %(buf[0])
                                remainingLength += (buf[0] & 127) * multiplier
                                multiplier *= 128

                                count += 1
                                if (buf[0] & 128) == 0:
                                    break

                            if count > 4:
                                break
                            print "remaining length = %i" %(remainingLength)
                            if remainingLength <= 0:
                                break
                            buf = bytearray(b" " * remainingLength)
                            # ret = s.recv_into(buf, remainingLength, MSG_WAITALL)
                            ret = s.recv_into(buf, remainingLength);

                            for value in buf:
                                print "%02x" %(value),
                            print " "
                            bufLenOfTopicFilter = bytearray(b" " * 2)
                            bufLenOfTopicFilter[0] = buf[0]
                            bufLenOfTopicFilter[1] = buf[1]
                            print "buf[0] is %i" %(buf[0])
                            print "buf[1] is %i" %(buf[1])
                            lenOfTopicFilter, = struct.unpack('>H', bufLenOfTopicFilter)


                            print "len of topic filter = %i" %(lenOfTopicFilter)
                            if lenOfTopicFilter > remainingLength:
                                break
                            bufTopicFilter = bytearray(b" " * lenOfTopicFilter)
                            for i in range(2, 2 + lenOfTopicFilter):
                                bufTopicFilter[i - 2] = buf[i]

                            # this bufTopicFilter is the topicFilter of the data which is received
                            # we can use this filter to judge the type of this command.
                            # or, judge whether it is a legaled/valided command.
                            print bufTopicFilter


                            bufRealData = buf[(2 + lenOfTopicFilter):]

                            # print "buf = %s" %(buf)
                            # start a threading to deal the data which is received
                            dealData= threading.Thread(target=DealMessage.dealData, args=(bufTopicFilter, str(bufRealData), remainingLength - 2 - lenOfTopicFilter))
                            dealData.setDaemon(True)
                            dealData.start()


                            # isockets_mqtt_dealData.dealData(str(bufRealData))

                    else:
                        # print tool.get_head_info()
                        print "should close socket"
                        closeSocket()
                        break

            for s in exceptional:
                print " exception condition on ", s.getpeername()
                #stop listening for input on the connection
                closeSocket()


def writeLoop():
    '''
    this fun is the socket write loop,
    :return:
    '''

    while(1):

        # use this semaphore to judge whether there are command message need to send or not.
        print "before socketSemaphore"
        socketSemaphore.acquire()
        print "after socketSemaphore"



        if not isCreated():
            global socketID
            print socketID
            createSocket()  #create socket
            print socketID
            socketSemaphore.release()
        else:
            global isServerConnected
            if not isServerConnected:
                global serverPort
                global serverIP
                print "serverIP = %s,    serverPort = %d" %(serverIP, serverPort)
                socketID.settimeout(10) # this used to set connect timeout
                ret = -1
                # try to connect to server
                try:
                    ret = socketID.connect_ex((serverIP, serverPort))
                except Exception as e:
                    print e
                    pass
                finally:
                    socketID.settimeout(None)  # set the timeout to default value

                    print "aa"
                    print ret


                if ret == 0:
                    print "success"
                    isServerConnected = True
                else:
                    print "failed"
                    closeSocket()   # if failed, so need to close socket.
                    isServerConnected = False
                    time.sleep(5)
                    socketSemaphore.release() #没有与服务器创建socket连接,则需要把线程信号量 +1, 启动重连

            else:
                isServerConnected = True


        # it is have connected to server
        if isServerConnected:
            pass
        else:
            continue


        sendBuf = []

        global isMQTTConnected
        global isMQTTSubscribe
        global commandArray

        if not isMQTTConnected:
            # send connect command
            sendBuf = MQTT_Package.Connect(connectIdentifier)
            for value in sendBuf:
                print "%02x " %(value),

        elif (not isMQTTSubscribe) and isMQTTConnected:
            # send subcribe command
            sendBuf = MQTT_Package.Subscribe(SUBSCRIBE_TOPIC)

            print "subscribe = "
            for value in sendBuf:
                print "%02x " %(value),
        else:
            if len(commandArray) == 0:
                continue
            else:
                if type(commandArray[0]) == str:
                    command = "MQTT_Package." + commandArray[0]
                    sendBuf = eval(command)()
                if type(commandArray[0]) == list:
                    print commandArray[0][0]
                    command = "MQTT_Package." + commandArray[0][0]
                    sendBuf = eval(command)(commandArray[0][1], commandArray[0][2], commandArray[0][3])

        ret = socketID.send(sendBuf)
        print ""
        print "after send", ret
        if ret > 0:
            if not isMQTTConnected:
                pass
            elif (not isMQTTSubscribe) and isMQTTConnected:
                pass
            else:
                print "remove commandArray[0]"
                commandArray = commandArray[1:]
            print "success"
        else:
            if not isMQTTConnected:
                socketSemaphore.release()
            elif (not isMQTTSubscribe) and isMQTTConnected:
                socketSemaphore.release()
            else:
                #
                pass

            print "failed"




def sendPINGREQ():
    """

    Args:


    Returns:

    """
    while True:
        global isMQTTConnected
        global isMQTTSubscribe
        if isMQTTSubscribe and isMQTTConnected:
            pass
        else:
            time.sleep(10)
            continue

        print "Send Ping REQ"
        commandArray.append("PINGREQ")
        socketSemaphore.release()
        time.sleep(30)



def addCommand(command):
    pass
