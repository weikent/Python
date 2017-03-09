#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import eyed3
import re
default_encoding = 'utf-8'

#phonetic transcription
# pt = [a:,?:,?:,i:,u:,?,?,?,i,u,e,?,au,?u,u?,ε?,i?,?i,ai,ei,p,t,f,k,θ,s,b,d,g,v,z,e,?,h,t,s,t,?,j,t,r,?,r,d,z,d,?,d,r,w,m,n,?,l]
# https://github.com/lukhnos/openvanilla
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def writeInfo(path, dirName, dirName1):
    """
    
    Arguments:
    - `dirName`:
    """
    #    print path, dirName
    if path[-3:] == "mp3":
        # tag = eyed3.Tag(path)
        # tag.remove(eyed3.ID3_V1)
        # tag.link(path)
        # tag.header.setVersion(eyed3.ID3_V2_3)
        # tag.setTextEncoding(eyed3.UTF_16_ENCODING)
        # tag.setAlbum(dirName)
        # tag.setArtist(dirName)
        # print dirName1
        # tag.setTitle(dirName1)
        # tag.update()
        print "cccc"
        print "aaaaa" + path
        print "bbbb" + dirName
        print "bbbb" + dirName1

        audiofile = eyed3.load(path)
        audiofile.initTag()
        # if audiofile.tag == None:
        #     audiofile.initTag()
        #     print "aaa"
        # else:
        #     print "ddd"
        #     pass

        print audiofile
        print "2",audiofile.tag.artist
        print audiofile.tag.album
        print audiofile.tag.title
        print dirName
#        print dirName1
        # listAlbum = dirName.split('.')

        
        
        # listTitle = dirName1.split('-')
        # print listTitle[0]
        # print listTitle[1]
        # if listTitle[0] == 'unit001':
        #     listTitle[0] += '动词'
        # elif listTitle[0] == 'unit002':
        #     listTitle[0] += '连词'
        # elif listTitle[0] == 'unit003':
        #     listTitle[0] += '关系词'
        # elif listTitle[0] == 'unit004':
        #     listTitle[0] += '非谓语动词'
        # elif listTitle[0] == 'unit005':
        #     listTitle[0] += '助动词'
        # elif listTitle[0] == 'unit006':
        #     listTitle[0] += '时态,语态'
        # elif listTitle[0] == 'unit007':
        #     listTitle[0] += '虚拟语气'
        # elif listTitle[0] == 'unit008':
        #     listTitle[0] += '副词'
        # elif listTitle[0] == 'unit009':
        #     listTitle[0] += '倒装句'
        # elif listTitle[0] == 'unit010':
        #     listTitle[0] += '比较结构'
        # elif listTitle[0] == 'unit011':
        #     listTitle[0] += '代词'
        # elif listTitle[0] == 'unit012':
        #     listTitle[0] += '复合形容词'
        # elif listTitle[0] == 'unit013':
        #     listTitle[0] += '介词'
        # elif listTitle[0] == 'unit014':
        #     listTitle[0] += '反问句'

        # audiofile.tag.artist = u'刘洪波听力真经'
        # audiofile.tag.album = u'刘洪波听力真经'
        # audiofile.tag.title = unicode(dirName1, 'utf-8')
        # audiofile.tag.save()

        #dirName1 = 'md5sum  /media/psf/Home/Documents/初级讲解/' + dirName1
        #os.system(dirName1)

        # print dirName.__class__
        # print dirName1.__class__
        # print dirName
        print "dd", dirName1
        audiofile.tag.artist = unicode("aa", 'utf-8')
        audiofile.tag.album = unicode("aa", 'utf-8')
        audiofile.tag.title = unicode(dirName1, 'utf-8')

        audiofile.tag.save()


def delFile(path):
    """
    
    Arguments:
    - `path`:
    """
    #    print path

    if path[-3:] == "mp3" or path[-3:] == "pdf" or path[-3:] == "txt" or path[-3:] == "rar":
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
        path = os.path.join(rootPath, dirName)
        #        print path
        if os.path.isdir(path):
#            changeInfo(rootPath, dirName)
            pass
        else:
            print "path = %s, folderName = %s, dirName = %s" % (path, folderName, dirName)
            writeInfo(path, folderName, dirName)


# delFile(path)


def changeInfo1(rootDir, folder):
    print "--------------------------------------------------------------------------------"
    rootDir = rootDir + "/"
    rootPath = os.path.join(rootDir, folder)
    print rootPath
    folderName = folder
    for dirName in os.listdir(rootPath):
        path = os.path.join(rootPath, dirName)
        print path
        if os.path.isdir(path):
            changeInfo(rootPath, dirName)
        else:
            print "path = ", path
            writeInfo(path, "101English")


# delFile(path)



# changeInfo("/media/psf/Home/Documents", "101英语短篇")
#changeInfo("/media/psf/Maxell/English/3.初级", "初级朗读")
#changeInfo("/media/psf/Maxell/English/3.初级", "初级讲解")
#changeInfo("/media/psf/Maxell/English/2.入门", "入门朗读")
#changeInfo("/media/psf/Maxell/English/2.入门", "入门讲解")
#changeInfo("/media/psf/Maxell/English", "6.语法")
#changeInfo("/media/psf/Maxell/", "声律启蒙")
#changeInfo("/media/psf/Maxell/", "笠翁对韵")
changeInfo("/Volumes/Maxell/English/雅思/刘洪波听力真经", "附录")

#changeInfo("/media/psf/Home/English/", "aa")
#changeInfo("/media/psf/Maxell/English/4.中级", "中级朗读")
#changeInfo("/media/psf/Maxell/English/4.中级", "中级讲解")
#changeInfo("/media/psf/Maxell/English/3.初级/", "初级朗读")
#changeInfo("/media/psf/Maxell/English/赖世雄", "0美语从头学美式音标")
#changeInfo("/media/psf/Maxell/English", "36篇")
#changeInfo("/media/psf/Maxell/English", "21美文")
# writeInfo("/media/psf/Home/Documents/书虫/牛津书虫第1级上(MP3+文本)/1A_01.爱情与金钱/1 Chapter 1.mp3", "1A_01.爱情与金钱")
# changeInfo("/media/psf/Home/Nutstore/ielts/听力/", "Day7")
# changeInfo("/media/psf/Maxell/English/雅思/雅思王/Chapter 5 吞音连读混合训练语料库", "01 横向测试")
