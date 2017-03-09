#!/usr/bin/env python
# -*- coding: utf-8 -*-



import os
import sys


os.

def changeName():
    print "aaa"
    rootPath = "/media/psf/Maxell/English/6.语法/"
    for dirName in os.listdir(rootPath): 
        print "path = ", dirName

        subName = dirName[4:-4]

        print "subName = ", subName
        list = subName.split("-")
        print list
        name1 = ""
        name2 = ""
        if len(list[0]) == 1:
            name1 = "00" + list[0]
        else:
            name1 = "0" + list[0]

        if len(list[0]) > 3:
            name1 = list[0][-3:]
        
        if len(list[1]) == 1:
            name2 = "00" + list[1]
        else:
            name2 = "0" + list[1]

        if len(list[1]) > 3:
            name2 = list[1][-3:]
        
        newName = dirName[:4] + name1 + "-" + name2 + dirName[-4:]
        print "newName = ", newName

        os.rename(rootPath + dirName, rootPath + newName)
        
changeName()
