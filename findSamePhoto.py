#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import hashlib

filename="./samePhoto"
filemd5= "./sameMd5"   # 用来保存2个相同的md5值的文件
f = 1
f2 = 2

list = []
dic = {}

def changeInfo(rootDir, folder):
    print "--------------------------------------------------------------------------------"
    rootDir = rootDir + "/"
    rootPath = os.path.join(rootDir, folder)
    print rootPath
    folderName = folder
    for dirName in os.listdir(rootPath):
        path = os.path.join(rootPath, dirName)
        #        print path
        if os.path.isdir(path):
            changeInfo(rootPath, dirName)
        else:
#            print "path = %s, folderName = %s, dirName = %s" % (path, folderName, dirName)
            doMd5(path)

#            f.write("%s,%s\r\n" %(path, hashlib.md5(path)))


def doMd5(path):
    m = hashlib.md5()
    with open(path, 'rb') as fp: 
        while True:
            blk = fp.read(4096) # 4KB per block
            if not blk: break
            m.update(blk)
        md5Str = m.hexdigest()
        print md5Str, path
        if md5Str in list:
#            f.write("%s, %s, repeat\r\n" % (path, md5Str))
            os.remove(path)
        else:
            #f.write("%s, %s, norepeat\r\n" % (path, md5Str))
            pass
        list.append(md5Str)
#        dic[md5Str] = path



def readFile(path):
    for line in open(path):
        list = line.split(',')
        print list[1], list[0]
        dic[list[1]] = list[0]

    #print dic



def checkFile(path):
    dic = {}
    f = open("checkFiel", "w+")


    for line in open(path):
        list = line.split(',')
#        print list[1], list[0]
        if list[1] in dic.keys():
#            f.write("%s, %s, %s\r\n" %(list[1], dic[list[1]], list[0]))
            os.remove(list[0])
        else:
            dic[list[1]] = list[0]


if __name__ == '__main__':
    # if os.path.exists(filename):
    #     os.remove(filename)
    # f = open(filename, "w+")

    # changeInfo("/Volumes/Seagate Expansion Drive/Photos","")

    # if os.path.exists(filemd5):
    #     os.remove(filemd5)
    # f2 = open(filemd5, "w+")


    # f = open(filename, "a")
    # readFile("./samePhoto1")
    changeInfo("/media/psf/Seagate Expansion Drive","Photos Library.photoslibrary")

    # checkFile(filename)
