#!/usr/bin/env python

import os,sys 
from cvedata.download import NvdLoad

"""
    Scan CVE For Linux System
"""

def cvescan():
    sys.path.append(os.getcwd()) 
    nvd = NvdLoad()

    try:
        nvd.run()
    except Exception, e:
        print e 
        sys.exit()

if __name__ == "__main__":
   cvescan() 
