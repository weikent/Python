#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import sys
import eyeD3
import re

def writeInfo(path, dirName,dirName1):
    """
    
    Arguments:
    - `dirName`:
    """
#    print path, dirName
    if path[-3 :] == "mp3":
        tag = eyeD3.Tag(path)
        tag.remove(eyeD3.ID3_V1)
        tag.link(path)
        tag.header.setVersion(eyeD3.ID3_V2_3)
        tag.setTextEncoding(eyeD3.UTF_16_ENCODING)
        tag.setAlbum(dirName)
        tag.setArtist(dirName)
        print dirName1
        tag.setTitle(dirName1)
        tag.update()
    

def delFile(path):
    """
    
    Arguments:
    - `path`:
    """
#    print path

    if path[-3 :] == "mp3" or path[-3 :] == "pdf" or path[-3 :] == "txt" or path[-3 :] == "rar":
        pass
    else:
        os.remove(path)

def changeInfo(rootDir, folder):

    print "--------------------------------------------------------------------------------"
    rootDir = rootDir + "/"
    rootPath = os.path.join(rootDir, folder)
    print rootPath
    folderName = folder
    for dirName in os.listdir(rootPath): 

#        print path 
        if os.path.isdir(path): 
            changeInfo(rootPath, dirName) 
        else:
            print "path = ", path
            writeInfo(path, folderName,dirName)
#            delFile(path)


def changeInfo1(rootDir, folder):

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
            print "path = ", path
            writeInfo(path, "101English")
#            delFile(path)



#changeInfo("/media/psf/Home/Documents", "101英语短篇")
changeInfo("/media/psf/Home/Documents", "书虫")

#writeInfo("/media/psf/Home/Documents/书虫/牛津书虫第1级上(MP3+文本)/1A_01.爱情与金钱/1 Chapter 1.mp3", "1A_01.爱情与金钱")