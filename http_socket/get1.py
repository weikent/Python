#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib

url = "http://127.0.0.1/cgi-bin/test.py?ServiceCode=aaaa"

conn = httplib.HTTPConnection("127.0.0.1")
conn.request(method="GET",url=url) 

response = conn.getresponse()
res= response.read()
print res