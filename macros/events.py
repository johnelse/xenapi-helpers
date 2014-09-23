from lib import XenAPI

def watch_objects(session, classes):
    token = ""
    timeout = 300.0
    timeout
    while True:
        result = session.xenapi.event.__getattr__("from")(classes, token, timeout)
        print "Got events:"
        for event in result["events"]:
            print event["id"]
        token = result["token"]

def watch_vm_by_name(session, vm_name):
    vms = session.xenapi.VM.get_by_name_label(vm_name)
    if len(vms) == 0:
        raise RuntimeError("No VM found")
    elif len(vms) > 1:
        raise RuntimeError("Multiple VMs found")
    else:
        watch_objects(session, ["VM/" + vms[0]])
