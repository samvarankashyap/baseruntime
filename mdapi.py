import requests
import pdb
import json
import pprint
import urllib

#pdb.set_trace()
URL = "https://apps.fedoraproject.org/mdapi"
branches = "/branches"
res = requests.get(URL+branches)
koji = "/koji/"

pkgs = json.loads(open("pkgout_json.txt","r").read())
count = 1
for p in pkgs:
    #res = requests.get(URL+koji+p["package_info"]["name"])
    res = urllib.urlopen(URL+koji+"pkg/"+p["package_info"]["name"]).read()
    #res = res.json()
    print(res)
    print("#################### src pkg")
    url = URL+koji+"srcpkg/"+p["package_info"]["name"]
    print url
    res = urllib.urlopen(url).read()
    print(res)
    print("#################### files")
    url = URL+koji+"files/"+p["package_info"]["name"]
    print url
    res = urllib.urlopen(url).read()
    print(res)
    print("#################### changelog")
    url = URL+koji+"changelog/"+p["package_info"]["name"]
    res = urllib.urlopen(url).read()
    print(res)
    count += 1
    print "###################################################",count,""
