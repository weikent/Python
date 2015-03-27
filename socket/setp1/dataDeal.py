#!/usr/bin/env python
# -*- coding: utf-8 -*-

class dataDeal(object):
    """
    """
    
    Mark1 = '~'                 # mark of Version1 
    Mark2 = '^'                 # mark of Version1.1
    
    # usr for struct.unpack
    dataFormat = '8s1B1H16s1B1H1H1Q'
    versionFormat = '8s'
    systemIDFormat = '1B'
    seqNumFormat = '1H'
    
    def __init__(self, ):
        """
        """
        
