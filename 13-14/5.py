def get_int_vlan_map(config):

    result_trunk = {}
    result_access = {}

    with open(config) as file:
        for line in file:
            if line.startswith('interface '):
                interface = line.split()[-1]
            elif line.startswith(' switchport trunk allowed vlan'):
                vlans = line.split()[-1]
                result_trunk[interface] = [vlan for vlan in vlans.split(',')]
            elif line.startswith(' switchport access vlan '):
                vlan = line.split()[-1]
                result_access[interface] = vlan

    return result_trunk, result_access

result = get_int_vlan_map('config_sw1.txt')
print(result)