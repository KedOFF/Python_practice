
from draw_network_graph import draw_topology
from task_15_2 import create_network_map

def unique_network_map(not_uniq_map):
    result = {}
    for ukey,value in not_uniq_map.items():
        if not result.get(value) == ukey:
            result[ukey] = value
    return(result)

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

net = create_network_map(infiles)
unet = unique_network_map(net)
print(unet)
draw_topology(unet, 'tst')
