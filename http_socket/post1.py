#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
#coding=utf8
 
import httplib, urllib
 
httpClient = None
try:
    params = urllib.urlencode({'maths': 'on'})
    headers = {"Content-type": "application/x-www-form-urlencoded"
                    , "Accept": "text/plain"
               , "Content" : "aaaaa"}
 
    httpClient = httplib.HTTPConnection("localhost", 80, timeout=30)
    httpClient.request("POST", "/cgi-bin/checkbox.cgi", params, headers)
 
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders() #获取头信息
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()