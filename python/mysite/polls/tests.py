# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

import sys
import os

#print os.getcwd()
sys.path.append('/Users/weishijian/Documents/Git/Python/python/mysite/')
sys.path.append('/Users/weishijian/Documents/Git/Python/python/mysite/mqtt')

from mqtt import myQ

print myQ.min(3,4)



