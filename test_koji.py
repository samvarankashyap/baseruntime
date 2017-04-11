import koji
session = koji.ClientSession('https://koji.fedoraproject.org/kojihub')
packagename = "zlib"
tables = session.queryHistory(package=packagename)
print tables.keys()
print("########################################################")
print("Group packages")
print("########################################################")
print tables["group_package_listing"]
print("########################################################")
print("tag packages")
print("########################################################")
print tables["tag_packages"]
print("########################################################")
print("Tag listing ")
print("########################################################")
print tables["tag_listing"]
print("########################################################")
print("Tag listing build id")
print("########################################################")
print tables["tag_listing"][0]["build_id"]


build_info = session.getBuild(tables["tag_listing"][0]["build_id"])
print "###################################3"
print build_info
task_id = build_info['task_id']
task = session.getTaskInfo(task_id, request=True)
print task
