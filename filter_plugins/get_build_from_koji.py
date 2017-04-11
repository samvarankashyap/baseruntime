#!/usr/bin/env python
import os
import sys
import koji
import operator

def get_build(session, pkg):
    """
    {
            "Architecture": "x86_64",
            "Build Date": "40 2017",
            "Build Host": "buildvm-06.phx2.fedoraproject.org",
            "Description": "",
            "Group": "Applications/File",
            "Install Date": "25 2017",
            "License": "GPLv3+ and GFDL",
            "Name": "gzip",
            "Packager": "Fedora Project",
            "Release": "2.module_60a31d5b",
            "Relocations": "(not relocatable)",
            "Signature": "(none)",
            "Size": "332299",
            "Source RPM": "gzip-1.8-2.module_60a31d5b.src.rpm",
            "Summary": "The GNU data compression program",
            "The gzip package contains the popular GNU gzip data compression": "The gzip package contains the popular GNU gzip data compression",
            "URL": "//www.gzip.org/",
            "Vendor": "Fedora Project",
            "Version": "1.8",
            "program. Gzipped files have a .gz extension.": "program. Gzipped files have a .gz extension."
        }
    """
    output = {}
    output["package_info"] = {}
    output["package_info"]["name"] = pkg["Name"]
    output["package_info"]["version"] = pkg["Version"]
    output["package_info"]["release"] = pkg["Release"]
    output["package_info"]["source_rpm"] = pkg["Source RPM"]
    package_name = pkg["Name"]
    version = pkg["Version"]
    release = pkg["Release"]
    src_rpm = pkg["Source RPM"]
    try:
        tables = session.queryHistory(package=package_name)
    except Exception as e:
        print(e)
        try:
            package_name = src_rpm.split("-")[0]
            tables = session.queryHistory(package=package_name)
        except Exception as e:
            print(e)
            try:
                package_name = "-".join(src_rpm.split("-")[0:2])
                tables = session.queryHistory(package=package_name)
            except Exception as e:
                print(e)
                return output
    try:
        tag_listing = tables["tag_listing"]
        tag_listing.sort(key=operator.itemgetter('build_id'), reverse=True)
        print tables["tag_listing"]
        for tag in tag_listing:
            print(tag)
            build_id = tag['build_id']
            build_info = session.getBuild(tag["build_id"])
            if (build_info["package_name"] == package_name) and \
               (build_info["version"] == version) and \
               (build_info["release"] == release):
                task_id = build_info['task_id']
                task = session.getTaskInfo(task_id, request=True)
                print("the task brought")
                print task
                output["build_info"] = task
                return output
    except Exception as e:
        print(e)
        return output
    return output


def get_build_from_koji(output):
    out = []
    session = koji.ClientSession('https://koji.fedoraproject.org/kojihub')
    for pkg in output:
        f_out = get_build(session, pkg)
        out.append(f_out)
    return out

class FilterModule(object):
    ''' A filter to fix network format '''
    def filters(self):
        return {
            'get_build_from_koji': get_build_from_koji
        }
