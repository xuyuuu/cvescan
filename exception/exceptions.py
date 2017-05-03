#!/usr/bin/env python

class CvescanException(Exception):
    """CVE Scan Exception"""

class CvescanMongodb(CvescanException):
    """MongoDB Exception"""

class CvescanNvddownload(CvescanException):
    """ Nvd Data download """ 

class CvescanJvnDownload(CvescanException):
    """ Jvn Data download """
