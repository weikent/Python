#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dateutil import tz  
from datetime import datetime  
  
# UTC Zone  
from_zone = tz.gettz('UTC')  
print from_zone
# China Zone  
to_zone = tz.gettz('CST')  
print to_zone
utc = datetime.utcnow()  
print utc
# Tell the datetime object that it's in UTC time zone  
utc = utc.replace(tzinfo=from_zone)  
print utc
# Convert time zone  
local = utc.astimezone(to_zone)  
print local
print datetime.strftime(local, "%Y-%m-%d %H:%M:%S")  



