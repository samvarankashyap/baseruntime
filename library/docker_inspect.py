# library/docker_inspect

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def _docker_inspect(module):

    results = {}
    cmd = "docker ps -q | xargs docker inspect"
    rc, out, err = module.run_command(cmd, use_unsafe_shell=True)
    docker = True
    try:
        docker_ds = json.loads(out)
    except:
        docker = False
    if docker:
        results = docker_ds
    
    return { 'ansible_facts': { 'docker_inspect': docker_ds } } 

def main():
    module = AnsibleModule(
        argument_spec = dict(
        ),  
        supports_check_mode = True,
    )   
    data = _docker_inspect(module)
    module.exit_json(**data)

from ansible.module_utils.basic import *
main()
