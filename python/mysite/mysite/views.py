#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import os
import sys
import json

from mqtt import DealMessage


def allDevices(request):
    #print DealMessage.getAllDevice()
    dict = DealMessage.getAllDevice()
    jsonStr = (json.dumps(dict)).encode('raw_unicode_escape')

    serverinfo = {}
    serverinfo["version"]= "mqtt1.0.0"
    serverinfo["port"] = "1883"

    strServerinfo = (json.dumps(serverinfo)).encode('raw_unicode_escape')

    #return HttpResponse(json.dumps(dict)  +  "\r\n" + jsonStr)
    #return HttpResponse(str)
    return render(request, 'index.html', {"devmap": jsonStr, "serverinfo" : strServerinfo})

