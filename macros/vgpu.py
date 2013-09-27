from lib import XenAPI

def create_vgpu_from_names(session, vm_name, gpu_group_name, vgpu_model_name):
    # Find suitable VMs.
    valid_vms = session.xenapi.VM.get_by_name_label(vm_name)
    if valid_vms == []:
        raise Exception("No VMs found")
    # Find suitable GPU groups.
    valid_gpu_groups = session.xenapi.GPU_group.get_by_name_label(gpu_group_name)
    if valid_gpu_groups == []:
        raise Exception("No GPU groups found")
    # Find suitable VGPU types.
    all_vgpu_types = session.xenapi.VGPU_type.get_all_records()
    iterator = all_vgpu_types.iteritems()
    def reduce_fn(acc, item):
        if item[1]["model_name"] == vgpu_model_name:
            return acc + [item[0]]
        else:
            return acc
    valid_vgpu_types = reduce(reduce_fn, iterator, [])
    if valid_vgpu_types == []:
        raise Exception("No VGPU types found")
    # Create the VGPU.
    return session.xenapi.VGPU.create( \
            valid_vms[0], \
            valid_gpu_groups[0], \
            "0", \
            {}, \
            valid_vgpu_types[0])
