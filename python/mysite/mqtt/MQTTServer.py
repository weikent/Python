#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'weishijian'

'''
此项目的主文件
'''
import threading

import time
import sys
# import MySocket
#
# import isockets_mqtt_socketCommand

print "start socket connect"


import MySocket


def start():
    MySocket.socketSemaphore.release()

    write = threading.Thread(target=MySocket.writeLoop)
    write.setDaemon(True)
    write.start()

    recv = threading.Thread(target=MySocket.readLoop)
    recv.setDaemon(True)
    recv.start()

    pingreq = threading.Thread(target=MySocket.sendPINGREQ)
    pingreq.setDaemon(True)
    pingreq.start()

    # MySocket.socketSemaphore.release()
    #
    # MySocket.socketSemaphore.release()
    #
    #
    # isockets_mqtt_socketCommand.commandConnect()
    #
    # isockets_mqtt_socketCommand.commandSubscribe()



    while(1):
        #time.sleep(10)
        payLoad = raw_input("input:")

        #    ret_topic_str = "isockets/Server/DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"  #2571B640054C837DD917206C00303330
        ret_topic_str = "isockets/Topic/052259B4630C1E46E672ACCD42DB4D16"
        commandList = ["Publish", ret_topic_str, payLoad, len(payLoad)]

        MySocket.commandArray.append(commandList)
        MySocket.socketSemaphore.release()

        print payLoad, "is you input"

        if payLoad == "q":
            print "you want to exit"

    print "exit"


    sys.exit()



if __name__ == '__main__':
    start()
