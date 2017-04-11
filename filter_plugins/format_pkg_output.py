#!/usr/bin/env python
import os
import sys
import abc
import StringIO
from ansible import errors

def format_pkg_output(output):
    f_out = {}
    output = output["results"]
    print("formatting output ::::::::::::")
    for item in output:
        f_out[item["item"]] = item["stdout_lines"]
    return f_out

class FilterModule(object):
    ''' A filter to fix network format '''
    def filters(self):
        return {
            'format_pkg_output': format_pkg_output
        }
