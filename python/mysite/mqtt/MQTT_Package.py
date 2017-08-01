#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'weishijian'

'''
此文件用于组建mqtt的消息包.

TODO: 在此文件中也完成mqtt的解包操作吧,把这些代码写成一个函数,供mysocket调用(这样在处理别的--非mqtt消息的时候,可以调用其他函数),
而不用把这些代码写在mysokcet文件中.
'''
import struct




MESSAGE_TYPE_CONNECT = 0x10
MESSAGE_TYPE_CONNACK = 0x20
MESSAGE_TYPE_PUBLISH = 0x30
MESSAGE_TYPE_SUBSCRIBE = 0x82
MESSAGE_TYPE_SUBACK = 0x90
MESSAGE_TYPE_PINGREQ = 0xC0
MESSAGE_TYPE_PINGRESP = 0xD0
MESSAGE_TYPE_DISCONNECT = 0xE0


PROTOCOL_NAME = "MQIsdp"
LEN_OF_PROTOCOL_NAME = len(PROTOCOL_NAME) + 2 # in mqtt, utf-8 string has two bytes at the front of the string.

PROTOCOL_LEVEL = 0x03
LEN_OF_PROTOCOL_LEVEL = 1

CONNECT_FLAG = 0x02
LEN_OF_CONNECT_FLAG = 1


KEEPALIVE = 60
LEN_OF_KEEPLIVE = 2



SUBSCRIBE_REQUEST_QOS = 0x00
LEN_OF_SUBSCRIBE_REQUEST_QOS = 1

LEN_PACKET_IDENTIFIER = 2
packetIdentifier = 1


def MakeUtf8String(string):
    """

    Args:
        string

    Returns:

    """
    len1 = len(string)

    bytes = bytearray(struct.pack('>H', len1))

    bytesString = bytearray(string)

    for value in bytesString:
        bytes.append(value)

    return bytes



def RemainingLength(remainingLength):
    """

    Args:
        remainingLength

    Returns:

    """
    lens = remainingLength

    buf = []
    while True:
        digit = lens % 128
        lens = lens / 128
        if lens > 0:
            digit = digit | 0x80
        else:
            pass

        buf.append(digit)

        if lens <= 0:
            break

    return buf

def Connect(clientIdentifier):
    """

    Args:
        clientIdentifier

    Returns:

    """

    connect = []
    connect.append(MESSAGE_TYPE_CONNECT)

    print len(connect)

    # add remaining length
    remainingLength = LEN_OF_PROTOCOL_NAME + LEN_OF_CONNECT_FLAG + LEN_OF_PROTOCOL_LEVEL + LEN_OF_KEEPLIVE + len(clientIdentifier) + 2
    bytes = RemainingLength(remainingLength)
    for value in bytes:
        connect.append(value)


    # add protocol name
    bytes = MakeUtf8String(PROTOCOL_NAME)
    for value in bytes:
        connect.append(value)

    # add protocol level
    connect.append(PROTOCOL_LEVEL)


    # add connect flags
    connect.append(CONNECT_FLAG)

    # add keep alive time
    bytes = struct.pack('>H', KEEPALIVE)
    connect.append(bytes[0])
    connect.append(bytes[1])

    # add clientIdentifier
    bytes = MakeUtf8String(clientIdentifier)
    for value in bytes:
        connect.append(value)

    print "before send connect"
    return bytearray(connect)




def Subscribe(topFilter):
    """

    Args:
        topFilter

    Returns:

    """

    subscribe = []
    subscribe.append(MESSAGE_TYPE_SUBSCRIBE)


    # add remainingLength
    remainingLength = len(topFilter) + 2 + LEN_PACKET_IDENTIFIER + LEN_OF_SUBSCRIBE_REQUEST_QOS
    bytes = RemainingLength(remainingLength)
    for value in bytes:
        subscribe.append(value)

    # add pack identifier
    bytes = struct.pack('>H', packetIdentifier)
    subscribe.append(bytes[0])
    subscribe.append(bytes[1])


    # add topic filter
    bytes = MakeUtf8String(topFilter)
    for value in bytes:
        subscribe.append(value)

    subscribe.append(SUBSCRIBE_REQUEST_QOS)

    print "before send subscribe"
    return bytearray(subscribe)


def Publish(topicFilter, payLoad, lenOfPayLoad):
    """

    Args:
        topFilter, payLoad, lenOfPayLoad

    Returns:

    """
    publish = []

    publish.append(MESSAGE_TYPE_PUBLISH)

    # add remaining length
    remainingLength = len(topicFilter) + 2 + lenOfPayLoad
    print "remainingLength = %d" %( remainingLength)

    bytes = RemainingLength(remainingLength)
    for value in bytes:
        print "%02x" %(value),
        publish.append(value)


    # add topic filter
    print "topci Filter binary code = "
    bytes = MakeUtf8String(topicFilter)
    for value in bytes:
        print "%02x" %(value),
        publish.append(value)

    print
    # add pay load
    payloadByteArr = bytearray(payLoad)
    for value in payloadByteArr:
        publish.append(value)

    print "publish Binary code"
    #for value in publish:
    #    print "%02x" %(value),

    print len(publish)
    return bytearray(publish)



def PINGREQ():
    """

    Args:


    Returns:

    """

    pingreq = []
    pingreq.append(MESSAGE_TYPE_PINGREQ)
    pingreq.append(0x00)
    print "Before Send PINGREQ"
    return bytearray(pingreq)




def RecvMessage(s):
    pass
