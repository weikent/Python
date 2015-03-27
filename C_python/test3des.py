#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf-8

import ctypes, os

import struct



if __name__ == "__main__":
    lib3des = ctypes.cdll.LoadLibrary(os.getcwd() + "/lib3des.so")
    # a = "aaa"
    # b = ctypes.c_char_p(a)
    # print b.value
    # print len(a)
    # print lib3des.encry(b, 3)
    # print b.value
    # print lib3des.decry(b, 8)
    # print b.value


##############################
    p = ctypes.create_string_buffer(10)  # 定义一个可变字符串变量，长度为 10 
    print p.raw 
    p.raw
    p.value = "aaa"
    print p[1]
    print lib3des.encry(p, 3)
    print p.value
    print lib3des.decry(p, 8)
    print p.value
    print p.raw

    print repr(p.raw)
    print p.value[5].decode()
    aa = '\x05'
    print aa
    print aa.decode()



    a=12.34
    bytes=struct.unpack('8b',p.value)

    print len(p.value)
    temp = p.value[0: len(p.value) - bytes[-1]]
    print temp

    print bytes
    print repr(p.value[5])
    # su = struct.unpack("3s5i", p.raw)
    # print su
    # s=struct.pack("2i13si6s2i", 33, 13, "www.baidu.com", 6, "冬季", 0, 0)
    # print s
    # us=struct.unpack("2i13si6s2i", s)
    # print us


