#!/usr/bin/env python

import os
import threading
import urllib
import gzip

def nvdload_task(url, file):
    try:
        urllib.urlretrieve(url, file)
        tmp = file + ".xml"
        w_f = open(tmp, "wb")
        r_f = gzip.open(file, "rb")
        while True:
            line = r_f.read(1024)
            if len(line) < 1:
                break
            w_f.write(line)
        r_f.close()
        w_f.close()
        os.remove(file)

    except Exception, e:
        print e

class CvescanThread(threading.Thread):
    def __init__(self, func, args, name=""):
       threading.Thread.__init__(self)
       self.func = func 
       self.args = args
       self.name = name

    def getResult(self):
        return self.res

    def run(self):
        self.res = apply(self.func, self.args)
