
from task_15_1 import parse_cdp_neighbors

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]
def create_network_map(filelist):
    result = {}
    for file in filelist:
        with open(file) as f:
            result.update(parse_cdp_neighbors(f.read()))
    return result

if __name__ == "__main__":
#    with open("sh_cdp_n_r3.txt") as f:
    print(create_network_map(infiles))
