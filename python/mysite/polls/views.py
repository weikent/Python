# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import sys
import os

#print os.getcwd()
sys.path.append('/Users/weishijian/Documents/Git/Python/python/mysite/')
#sys.path.append('/Users/weishijian/Documents/Git/Python/python/mysite/mqtt')



def index(request):
    return HttpResponse("aaaaa")
