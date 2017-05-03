#!/usr/bin/env python

import os
import threading
import re
from exception.exceptions import *
from task.cvescanthread import * 


class NvdLoad(object):
    """
        Download NVD 
    """

    def __init__(self, baseurl = "https://static.nvd.nist.gov/feeds/xml/cve/2.0/nvdcve-2.0-unknow.xml.gz"):
        nvdyears = ["2012", "2013", "2014", "2015", "2016", "2017"]
        self._baseurl = baseurl
        self._urls = []
        self._tasks = []
        for year in nvdyears:
            url = re.sub("unknow", year, baseurl)
            self._urls.append(url)
            
            file = os.getcwd()+ "/cvedata/data/" + year + ".gz"
            thread = CvescanThread(nvdload_task, (url, file), nvdload_task.__name__)
            self._tasks.append(thread)


    def run(self):
        try:
            for task in self._tasks:
                task.start()
                task.join()
        except Exception, e:
            raise CvescanNvddownload("Nvd Download Exception...")

        

class JvnLoad(object):
    """ 
        Download Jvn
    """

    def __init__():
        pass

