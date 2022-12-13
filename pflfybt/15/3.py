from task_11_2 import create_network_map
from pprint import pprint
from draw_network_graph import draw_topology

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def unique_network_map(topology_dict):
    """
    Функция обрабатывает словарь содинений и удаляет дублирующиеся значения.
    topology dict - ожидает в качестве аргумента словарь, полученный с помощью функции create_network_map.
    Функция возвращает словарь, описывающий соединения между устройствами.
    """
    general_map = {}
    for key,value in topology_dict.items():
        if not general_map.get(value) == key:
            general_map[key] = value
    return(general_map)


if __name__ == "__main__":
    topology = create_network_map(infiles)
    unique_topology = unique_network_map(topology)
    vizual_topology = draw_topology(unique_topology)
    pprint(unique_topology)
