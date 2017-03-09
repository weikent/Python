import os
import sys


def changeName():
    rootPath = "/Users/weishijian/Nutstore/work/2016-12-2/1"
    for parent,dirnames, filenames in os.walk(rootPath):
        # print rootPath
        # print parent
        # print dirnames
        # print filenames

        for filename in filenames:
            print filename[:-4]



changeName()
