#!/usr/bin/env python
# -*- coding: utf-8 -*-



import os

def changeName():
    print "aaa"
    rootPath = "/media/psf/Maxell/English/3.初级/初级讲解/"
    for dirName in os.listdir(rootPath): 
        print "path = ", dirName

        subName = dirName[1:-10]
        newSubName = ""
        if len(subName) == 1:
            newSubName = "00" + subName
        if len(subName) == 2:
            newSubName = "0" + subName
        if len(subName) == 3:
            newSubName = subName
        
        
        

        print "newSubName = ", newSubName
        
        
        newName = dirName[:1] + newSubName + dirName[-10:]
        print "newName = ", newName

        os.rename(rootPath + dirName, rootPath + newName)
        
changeName()
