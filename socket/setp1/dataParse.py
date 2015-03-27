#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ctypes
import struct
import os



class dataParse(object):
    """

    """
    parseStr = ""
    def __init__(self, ):
        """
        """

    def parse(self, data):
        """
        
        Arguments:
        - `self`:
        
        """
        print "parse" , len(data)
        if data[0] == '^':
            print "this is Version 1.1"
        else:
            return
#        print data
        messageLen = data[1: 5]

        format = ">1i"
        len_ = struct.unpack(format, messageLen)
        print len_

        data2 = data[5:]
        

        lib3des = ctypes.cdll.LoadLibrary(os.getcwd() + "/../lib3des.so")
        p = ctypes.create_string_buffer(len_[0])
        p.value = data2
        print "len of data2 = " , len(data2)
        lib3des.decry(p, len_[0])
        print p.value
        print "----------------------------------------"
        print ctypes.sizeof(p)
        
        print repr(p.raw)
        print p.raw , "--------------------------------------------------"
        dataFormat = '8s1B1H16s1B1H1H1Q'
        version = p.raw[0:8]
        print repr(version)
        print version
#        dddd = struct.unpack('8s', p.value[0:9])
#        print dddd

        systemID = p.raw[8:9]
        print repr(systemID)
        nSystemID = struct.unpack('>1B', systemID)
        print nSystemID
        
