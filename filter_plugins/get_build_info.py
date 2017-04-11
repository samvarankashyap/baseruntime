#!/usr/bin/env python
import os
import sys
import abc
import StringIO
from ansible import errors

def get_build_info(output):
    out = []
    print("formatting output ::::::::::::")
    """
    zlib-1.2.11-2.module_60a31d5b.x86_64": [
            "Name        : zlib",
            "Version     : 1.2.11",
            "Release     : 2.module_60a31d5b",
            "Architecture: x86_64",
            "Install Date: Fri Apr  7 00:00:21 2017",
            "Group       : System Environment/Libraries",
            "Size        : 194423",
            "License     : zlib and Boost",
            "Signature   : (none)",
            "Source RPM  : zlib-1.2.11-2.module_60a31d5b.src.rpm",
            "Build Date  : Wed Mar 15 16:52:24 2017",
            "Build Host  : buildvm-11.phx2.fedoraproject.org",
            "Relocations : (not relocatable)",
            "Packager    : Fedora Project",
            "Vendor      : Fedora Project",
            "URL         : http://www.zlib.net/",
            "Summary     : The compression and decompression library",
            "Description :",
            "Zlib is a general-purpose, patent-free, lossless data compression",
            "library which is used by many different programs."
        ]
    """
    for pkg in output:
        f_out = {}
        pkg_info = output[pkg]
        pkg_info.pop()
        pkg_info.pop()
        for ele in pkg_info:
            key = ele.split(":")[0].strip()
            value = ele.split(":")[-1].strip()
            f_out[key] = value
        out.append(f_out)
    return out

class FilterModule(object):
    ''' A filter to fix network format '''
    def filters(self):
        return {
            'get_build_info': get_build_info
        }
